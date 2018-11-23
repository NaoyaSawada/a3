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
from a3.model import Application

#
# アカウント関連の操作
#
@view_defaults(route_name = 'api::v1:applications', renderer = 'json')
class ApplicationsController:
	#
	# コンストラクタ
	#
	def __init__(self, request):
		self.request = request

	#
	# 一覧取得処理
	#
	@view_config(request_method = 'GET')
	def get(self):
		#
		# アカウントの検索
		#
		session = SessionFactory.createSession()

		#
		# アプリケーション一覧の取得 & 詳細情報取得
		#
		applications = session.query(Application).all()
		apps = [app.to_dict() for app in applications]

		#
		# OK を 返す
		#
		return OK(apps)

	#
	# 新規登録処理
	#
	@view_config(request_method = 'POST')
	def post(self):
		#
		# JSON の 書式定義
		#
		schema = {
			'type'		: 'object',
			'properties'	: {
				'name' : {
					'type'		: 'string',
				},
				'callback_url' : {
					'type'		: 'string',
					'format'	: 'email'
				}
			},
			#
			# 追加の引数を許可しない
			#
			'additionalProperties'	: False,
			'required'		: ['name', 'callback_url'],
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
		name = self.request.json_body['name']
		callback_url = self.request.json_body['callback_url']

		#
		# 既に登録済みのメールアドレスか確認
		#
		session = SessionFactory.createSession()

		#
		# DB へ 登録
		#
		application = Application(name, callback_url)
		session.add(application)
		session.commit()

		#
		# トークンを返す
		#
		return OK()

