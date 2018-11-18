#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import requests

#
# アクセス用ベースURL
#
url = 'http://127.0.0.1:1103'

#
# アカウント関連のテスト
#
class AccountService(unittest.TestCase):
	#
	# サインアップのテスト
	#
	def test_signup(self):
		response = requests.post(
			'%s/api/v1/accounts/' %(url),
			json = {
				'mail'		: 'naoya@abc.com',
				'password'	: 'qwertyuiop'
			}
		)
		#print(response.content)
		self.assertEqual(response.status_code, 200)

	#def test_stop_bacnetd(self):
	#	response = requests.delete('%s/api/v1/service/bacnetd/' %(url))
	#	#print(response.content)
	#	self.assertEqual(response.status_code, 200)

