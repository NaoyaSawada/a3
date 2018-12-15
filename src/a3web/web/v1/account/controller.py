#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults

#
# アカウント関連の操作
#
@view_defaults(route_name = 'web::v1:accounts', renderer = 'json')
class AccountsController:
	#
	# コンストラクタ
	#
	def __init__(self, request):
		self.request = request

	#
	# サインイン処理
	#
	@view_config(request_method = 'GET', renderer='./templates/index.html')
	def signin(self):
		session = self.request.session
		if not 'counter' in session:
			session['counter'] = 0
		session['counter'] = session['counter'] + 1
		print session['counter']
		return {}

	#
	# サインアップ処理
	#
	@view_config(request_method = 'POST')
	def signup(self):
		return True

	#
	# サインアップ処理の確認
	#
	@view_config(request_method = 'PATCH')
	def validate(self):
		return True
