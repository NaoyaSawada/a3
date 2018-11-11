#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults

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
	#	pass

	#
	# サインアップ処理
	#
	@view_config(request_method = 'POST')
	def signup(self):
		pass

