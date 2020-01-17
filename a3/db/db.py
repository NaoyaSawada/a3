#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

#
# SQLAlchemy
#
from sqlalchemy import engine_from_config, pool
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from alembic.config import Config

#
# スクリプトを実行するディレクトリ設定
#
from a3 import base_path, config_path
os.chdir(base_path)

#
# SQL エンジンの取得
#
config = ConfigParser()
config.read(config_path)
Engine = engine_from_config(
	config['alembic'],
	prefix = 'sqlalchemy.',
	poolclass = pool.NullPool
)

#
# SQL接続用セッションオブジェクト化
#
session_factory = sessionmaker(bind = Engine)
Session = scoped_session(session_factory)

#
# セッションの取得
#
class SessionFactory:
	#
	# コンストラクタ
	#
	def __init__(self):
		self.sesion = None

	#
	# セッション取得
	#
	@classmethod
	def createSession(cls):
		return Session()

	#
	# ENTER
	#
	def __enter__(self):
		self.session = Session()
		return self.session

	#
	# EXIT
	#
	def __exit__(self, type, value, traceback):
		self.session.close()
		return True

#
# Entry Point
#
if __name__ == "__main__":
	session = Session() 
	help(session)

