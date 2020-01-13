#!/usr/bin/env python
# -*- coding: utf-8 -*-
from a3.model import BaseObject
from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey

#
# UUID & HASH
#
import uuid
import hashlib, binascii

#
# アカウント
#
class Account(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_ACCOUNT'

	#
	# カラム定義
	#
	id	= Column('ID', String(1024), primary_key=True)
	mail	= Column('MAIL', String(1024))
	hash	= Column('HASH', String(1024))
	lock	= Column('LOCK', BOOLEAN)

	#
	# コンストラクタ
	#
	def __init__(self, mail, password):
		self.id = str(uuid.uuid4())
		self.mail = mail
		self.hash = self.getHash(password, self.id)
		self.lock = True

	#
	# ハッシュ化
	#
	def getHash(self, password, salt):
		dk = hashlib.pbkdf2_hmac('sha256', password, salt, 1024)
		return binascii.hexlify(dk)

	#
	# アンロック
	#
	def unlock(self):
		self.lock = False

	#
	# パスワードの確認
	#
	def validate(self, password):
		#
		# パスワードのハッシュを確認
		#
		if self.hash == self.getHash(password, self.id):
			return True
		return False

	#
	# 文字列化
	#
	def __str__(self):
		return '<Account id=%s mail=%s>' %(self.id, self.mail)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'	: self.id,
			'mail'	: self.mail,
			'hash'	: self.hash
		}

