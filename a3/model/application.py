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
	id		= Column('ID', String(1024), primary_key=True)
	name		= Column('NAME', String(1024))
	callback_url	= Column('CALLBACK_URL', String(1024))

	#
	# コンストラクタ
	#
	def __init__(self, name, callback_url):
		self.id = str(uuid.uuid4())
		self.name = name
		self.callback_url = callback_url

	#
	# 文字列化
	#
	def __str__(self):
		return '<Application id=%s name=%s>' %(self.id, self.name)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'id'		: self.id,
			'name'		: self.name,
			'callback_url'	: self.callback_url
		}

