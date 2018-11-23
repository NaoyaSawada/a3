#!/usr/bin/env python
# -*- coding: utf-8 -*-
from driver import MemoryCacheDriver

#
# CacheManeger
#
class CacheManeger:
	#
	# インスタンス保持用変数
	#
	_instance = None
	_driver = None

	#
	# get Instance
	#
	@classmethod
	def getInstance(cls):
		if cls._instance is None:
			cls._instance = cls()
			cls._driver = MemoryCacheDriver()
		return cls._instance

	#
	# ドライバ内の名前空間を返す
	#
	@classmethod
	def getNamespace(cls, name):
		#
		# インスタンス取得
		#
		CacheManeger.getInstance()
		return cls._driver.getNamespace(name)

#
# Entry Point
#
if __name__ == '__main__':
	pass

