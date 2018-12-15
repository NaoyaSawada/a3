#!/usr/bin/env python
# -*- coding: utf-8 -*-
import account

#
# Bootstrap Code
#
def bootstrap(config):
	#
	# Scan controller
	#
	config.add_route('web::v1:accounts', '/')
        config.include(account.bootstrap)

#
# Make bootstrap attribute
#
__all__ = [bootstrap]

