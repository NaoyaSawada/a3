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
# グループ
#
class Group(BaseObject):
	#
	# テーブル名
	#
	__tablename__ = 'M_GROUP'

	#
	# カラム定義
	#
	id      = Column('ID', String(1024), primary_key=True)
	name	= Column('NAME', String(1024))

	#
	# コンストラクタ
	#
	def __init__(self, name):
		self.id		= str(uuid.uuid4())
		self.name	= name

	#
	# 文字列化
	#
	def __str__(self):
		return '<Group name=%s>' %(self.name)

	#
	# 辞書化
	#
	def to_dict(self):
		return {
			'name'		: self.name,
		}

