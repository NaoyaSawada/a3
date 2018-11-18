#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

#
# Alembic による DB の 更新を実行
#
def doAlembicUpgradeHead():
	#
	# スクリプトを実行するディレクトリ設定
	#
	base_path = os.path.dirname(os.path.abspath(__file__))
	os.chdir(base_path + '/../')

	#
	# DB を 最新のスキーマ へ アップデート
	#
	command = ['alembic upgrade head']
	subprocess.check_call(command, shell=True)

