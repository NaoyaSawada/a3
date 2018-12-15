#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyramid.session import SignedCookieSessionFactory
session_factory = SignedCookieSessionFactory('tuntunkun')

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
	# Include Template Engne
	#
	config.include('pyramid_jinja2')
	config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')

	#
	# Session Library Configuration
	#
	config.set_session_factory(session_factory)

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

