#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cachetools import TTLCache

#
# CacheManeger
#
class CacheManeger:
	#
	# インスタンス保持用変数
	#
	_instance = None
	_dict = None

	#
	# get Instance
	#
	@classmethod
	def getInstance(cls):
		if cls._instance is None:
			cls._instance = cls()
			cls._dict = TTLCache(maxsize=1024, ttl=3600)
		return cls._instance

	#
	# set
	#
	def set(self, key, value):
		self._dict[key] = value

	#
	# get
	#
	def get(self, key):
		if key in self._dict:
			return self._dict[key]
		return None

if __name__ == '__main__':
	cache = CacheManeger.getInstance()
	cache.set('aa', 1)
	cache.set('aa', 1)

