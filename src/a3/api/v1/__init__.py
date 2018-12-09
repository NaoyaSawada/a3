#!/usr/bin/env python
# -*- coding: utf-8 -*-
import account
import application
import ticket

#
# Bootstrap Code
#
def bootstrap(config):
	#
	# Scan controller
	#
	config.add_route('api::v1:accounts', '/accounts/')
	config.add_route('api::v1:applications', '/applications/')
	config.add_route('api::v1:tickets', '/tickets/')
	config.add_route('api::v1:tickets:[ticket]', '/tickets/{ticket}')
        config.include(account.bootstrap)
        config.include(application.bootstrap)
        config.include(ticket.bootstrap)

#
# Make bootstrap attribute
#
__all__ = [bootstrap]

