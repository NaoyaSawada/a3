#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.view import view_config, view_defaults

#
# アカウント関連の操作
#
@view_defaults(route_name = 'api::v1:account', renderer = 'json')
class AccountController:
	#
	# コンストラクタ
	#
	def __init__(self, request):
		self.request = request

	#
	# サインイン処理
	#
	def signup(self):
		pass

	#
	# サインアップ処理
	#
	def signup(self):
		pass

