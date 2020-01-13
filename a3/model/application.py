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
class Application(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_APPLICATION'

	#
	# カラム定義
	#
	key		= Column('KEY', String(1024), primary_key=True)
	secret		= Column('SECRET', String(1024))
	name		= Column('NAME', String(1024))
	callback_url	= Column('CALLBACK_URL', String(1024))

	#
	# コンストラクタ
	#
	def __init__(self, name, callback_url):
		self.key		= str(uuid.uuid4())
		self.secret		= str(uuid.uuid4())
		self.name		= name
		self.callback_url	= callback_url

	#
	# 文字列化
	#
	def __str__(self):
		return '<Application name=%s>' %(self.name)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'name'		: self.name,
			'callback_url'	: self.callback_url
		}

