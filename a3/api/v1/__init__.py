#!/usr/bin/env python
# -*- coding: utf-8 -*-
import account
import application

#
# Bootstrap Code
#
def bootstrap(config):
	#
	# Scan controller
	#
	config.add_route('api::v1:accounts', '/accounts/')
	config.add_route('api::v1:applications', '/applications/')
        config.include(account.bootstrap)
        config.include(application.bootstrap)

#
# Make bootstrap attribute
#
__all__ = [bootstrap]

