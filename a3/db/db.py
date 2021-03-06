#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#
# SQLAlchemy
#
from sqlalchemy import engine_from_config, pool
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
import pkg_resources

#
# スクリプトを実行するディレクトリ設定
#
base_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.abspath(os.path.join(base_path, '../'))
os.chdir(base_path)

#
# SQL エンジンの取得
#
config = Config(pkg_resources.resource_filename('a3', 'alembic.ini'))
Engine = engine_from_config(
	config.get_section(config.config_ini_section),
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

