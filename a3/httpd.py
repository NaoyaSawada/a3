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
@click.option('--port', '-p', default = 1103)
def start_httpd(host, port):
	#
	# WEB アプリケーションの設定
	#
	config = Configurator()

	#
	# API V1 の 読み込み
	#
	import api.v1
	config.include(api.v1.bootstrap, route_prefix='api/v1/')

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

