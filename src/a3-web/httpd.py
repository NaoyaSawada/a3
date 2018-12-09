#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Command Line Utility
#
import click

#
# Web Application Framework
#
from waitress import serve
from pyramid.config import Configurator

#
# Start HTTPD
#
@click.command()
@click.option('--host', '-h', default = '0.0.0.0')
@click.option('--port', '-p', default = 1180)
def start_httpd(host, port):
	#
	# WEB アプリケーションの設定
	#
	config = Configurator()

	#
	# WEB UI の 読み込み
	#
	import web.v1
	config.include(web.v1.bootstrap)

	#
	# HTTPDサーバの設定
	#
	app = config.make_wsgi_app()
	serve(app, host=host, port=port)

#
# Entry Point
#
if __name__ == '__main__':
	start_httpd()

