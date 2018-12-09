#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cachetools import TTLCache

#
# MemoryCache
#
class MemoryCache:
	#
	# コンストラクタ
	#
	def __init__(self):
		self._cache = TTLCache(maxsize=1024, ttl=3600)

	#
	# set
	#
	def set(self, key, value):
		self._cache[key] = value

	#
	# get
	#
	def get(self, key):
		if key in self._cache: return self._cache[key]
		return None

	#
	# delete
	#
	def delete(self, key):
		return self._cache.pop(key)

#
# MemoryCache
#
class MemoryCacheDriver:
	def __init__(self):
		self.namespaces = dict()

	def getNamespace(self, name):
		if not name in self.namespaces:
			self.namespaces[name] = MemoryCache()
		return self.namespaces[name]

#
# Entry Point
#
if __name__ == '__main__':
	driver = MemoryCacheDriver()
	cache = driver.getNamespace('test')
	cache.set('aa', 1)
	cache.set('aa', 1)
	cache.delete('aa')
	cache.set('bb', 1)

