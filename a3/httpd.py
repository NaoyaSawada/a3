#!/usr/bin/env python
# -*- coding: utf-8 -*-
from waitress import serve
from pyramid.config import Configurator

#
# Start HTTPD
#
def start_httpd(host = '0.0.0.0', port = 1103):
	#
	# WEB アプリケーションの設定
	#
	config = Configurator()

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

