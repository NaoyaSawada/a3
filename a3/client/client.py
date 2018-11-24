#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

class A3Client:
	#
	# コンストラクタ
	#
	def __init__(self, host = '127.0.0.1', port = 1103):
		self.url = 'http://%s:%d' %(host, port)

	#
	# サインイン
	#
	def signin(self, mailaddr, password):
		#
		# クエリ作成
		#
		query = '%s/api/v1/tickets/' %(self.url)

		#
		# 認証の実行
		#
		response = requests.post(query, json = {
			'mail'		: mailaddr,
			'password'	: password
		})

		#
		# 結果の返却
		#
		json = response.json()
		ok = json['ok']
		ticket = None
		if ok == True:
			ticket = json['data']['ticket']
		return ok, ticket

	#
	# チケットの確認
	#
	def validate(self, ticket):
		#
		# クエリ作成
		#
		query = '%s/api/v1/tickets/%s' %(self.url, ticket)

		#
		# チケットの確認
		#
		response = requests.get(query)
		json = response.json()
		return json['ok']

if __name__ == '__main__':
	client = Client()
	ok, ticket = client.signin('naoya@tuntunkun.com', 'test')
	print client.validate(ticket)

