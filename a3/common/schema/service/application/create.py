#
# JSON の 書式定義
#
schema = {
	'type'		: 'object',
	'properties'	: {
		'name' : {
			'type'		: 'string',
		},
		'callback_url' : {
			'type'		: 'string',
			'format'	: 'uri'
		}
	},
	#
	# 追加の引数を許可しない
	#
	'additionalProperties'	: False,
	'required'		: ['name'],
}

