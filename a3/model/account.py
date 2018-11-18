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
	uuid	= Column('UUID', String(1024), primary_key=True)
	mail	= Column('MAIL', String(1024))
	hash	= Column('HASH', String(1024))
	lock	= Column('LOCK', BOOLEAN)

	#
	# コンストラクタ
	#
	def __init__(self, mail, password):
		self.uuid = str(uuid.uuid4())
		self.mail = mail
		self.hash = self.getHash(password, self.uuid)
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
	# 文字列化
	#
	def __str__(self):
		return '<Account uuid=%s mail=%s>' %(self.uuid, self.mail)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'uuid'	: self.uuid,
			'mail'	: self.mail,
			'hash'	: self.hash
		}

