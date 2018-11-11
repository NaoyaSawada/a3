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
	config.add_route('api::v1:accounts', '/accounts/')
        config.include(account.bootstrap)

#
# Make bootstrap attribute
#
__all__ = [bootstrap]

