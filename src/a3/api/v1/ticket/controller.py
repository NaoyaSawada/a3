#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults

#
# JSON Validation
#
import jsonschema

#
# API Response
#
from a3.api.common.response import OK, Error

#
# Database
#
from a3.db import SessionFactory
from a3.model import Account

#
# Cache Manager
#
import uuid
from a3.cache import CacheManeger

#
# チケット(ユーザ認証した事を示す)
#
@view_defaults(route_name = 'api::v1:tickets', renderer = 'json')
class TicketsController:
	#
	# コンストラクタ
	#
	def __init__(self, request):
		self.request = request

	#
	# サインイン処理
	#
	@view_config(request_method = 'POST')
	def signin(self):
		#
		# JSON の 書式定義
		#
		schema = {
			'type'		: 'object',
			'properties'	: {
				'mail' : {
					'type'		: 'string',
					'format'	: 'email'
				},
				'password' : {
					'type'		: 'string',
				},
			},
			#
			# 追加の引数を許可しない
			#
			'additionalProperties'	: False,
			'required'		: ['mail', 'password'],
		}

		#
		# 書式チェックの実施
		#
		try:
			jsonschema.validate(
				self.request.json_body,
				schema,
				format_checker=jsonschema.FormatChecker()
			)
		#
		# JSON内のデータ書式に問題がある場合
		#
		except jsonschema.ValidationError as e:
			return Error(e.message)
		#
		# JSONの書式に問題がある場合
		#
		except ValueError:
			return Error('JSON Syntax error...')

		#
		# バリデーション結果の取得
		#
		mail = self.request.json_body['mail']
		password = self.request.json_body['password']

		#
		# アカウントの検索
		#
		session = SessionFactory.createSession()
		account = session.query(Account).filter_by(mail = mail).first()

		#
		# アカウントが存在しパスワードが正しいかを確認
		#
		if not account == None and account.validate(password) == True:
			#
			# アカウント検証用 の トークンの発行 & 保存
			#
			ticket = str(uuid.uuid4())
			cache = CacheManeger.getNamespace('signin:ticket')
			cache.set(ticket, account.id)

			#
			# チケットを返す
			#
			return OK({ 'ticket' : ticket })
		return Error('Username or Password is invalid...')

#
# チケット(ユーザ認証した事を示す)
#
@view_defaults(route_name = 'api::v1:tickets:[ticket]', renderer = 'json')
class TicketController:
	#
	# コンストラクタ
	#
	def __init__(self, request):
		self.request = request

	#
	# チケットの有効性確認
	#
	@view_config(request_method = 'GET')
	def validate(self):
		#
		# チケットID の 取得
		#
		ticket = self.request.matchdict['ticket']

		#
		# チケットの検証
		#
		cache = CacheManeger.getNamespace('signin:ticket')
		if cache.get(ticket) == None:
			return Error('Ticket alredy expired...')
		return OK()

