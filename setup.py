#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

#
# requirement.txt 内の依存ライブラリの読み込み処理
#
def _load_requires_from_file(filepath):
	return [pkg_name.rstrip('\n') for pkg_name in open(filepath).readlines()]

#
# requirement.txt 内のファイルのインストール処理
#
def _install_requires():
	return _load_requires_from_file('requirements.txt')

#
# Entry point
#
if __name__ == '__main__':
	setup(
		#
		# Software Information
		#
		name		= 'a3',
		version		= '0.6.0',

		#
		# Author Information
		#
		author		= 'Naoya Sawada',
		author_email	= 'naoya@tuntunkun.com',

		#
		# Package Information
		#
		packages	= find_packages(),
		install_requires= _install_requires(),
		package_dir	= { 'a3' : 'a3' },
	)

