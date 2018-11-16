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
from model import Account

#
# Cache Manager
#
import uuid
from a3.cache import CacheManeger
#
# アカウント関連の操作
#
@view_defaults(route_name = 'api::v1:accounts', renderer = 'json')
class AccountsController:
	#
	# コンストラクタ
	#
	def __init__(self, request):
		self.request = request

	#
	# サインイン処理
	#
	#@view_config(request_method = 'GET')
	#def signin(self):
	#	return OK()

	#
	# サインアップ処理
	#
	@view_config(request_method = 'POST')
	def signup(self):
		#
		# JSON の 書式定義
		#
		schema = {
			'type'		: 'object',
			'properties'	: {
				'mail' : {
					'type'		: 'string',
					'oneOf'		: [{ 'format' : 'email' }]
				},
				'password' : {
					'type'		: 'string',
				}
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
			jsonschema.validate(self.request.json_body, schema)
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
		# 既に登録済みのメールアドレスか確認
		#
		session = SessionFactory.createSession()
		account = session.query(Account).filter_by(mail = mail).first()
		if not account == None:
			return Error('Account already exist...')

		#
		# DB へ 登録
		#
		account = Account(mail, password)
		session.add(account)
		session.commit()

		#
		# アカウント検証用 の トークンの発行 & 保存
		#
		token = str(uuid.uuid4())
		cache = CacheManeger.getInstance()
		cache.set(token, account.uuid)

		#
		# トークンを返す
		#
		return OK({ 'token' : token })

	#
	# サインアップ処理の確認
	#
	@view_config(request_method = 'PATCH')
	def validate(self):
		#
		# JSON の 書式定義
		#
		schema = {
			'type'		: 'object',
			'properties'	: {
				'token' : {
					'type'		: 'string',
					'oneOf'		: [{ 'format' : 'uuid' }]
				},
			},
			#
			# 追加の引数を許可しない
			#
			'additionalProperties'	: False,
			'required'		: ['token'],
		}

		#
		# 書式チェックの実施
		#
		try:
			jsonschema.validate(self.request.json_body, schema)
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
		token = self.request.json_body['token']

		#
		# トークンのアカウント取得
		#
		cache = CacheManeger.getInstance()
		account_uuid = cache.get(token)
		if account_uuid == None:
			return Error('This token is already expired...')

		#
		# DB へ メールアドレスの登録
		#
		session = SessionFactory.createSession()
		account = session.query(Account).filter_by(uuid = account_uuid).first()
		if account == None:
			return Error('This token is already expired...')

		#
		# アカウントロックの解除
		#
		account.unlock()
		session.commit()
		cache.delete(token)

		#
		# アカウントの発行処理
		#
		return OK()

