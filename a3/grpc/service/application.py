from a3.grpc.interface.response_pb2 import *
from a3.grpc.interface.application_pb2 import *
from a3.grpc.interface.application_pb2_grpc import ApplicationServicer
from google.protobuf.json_format import MessageToDict

import jsonschema
from a3.common.schema.service.application import create

#
# Database
#
from a3.db import SessionFactory
from a3.model import Application

class ApplicationService(ApplicationServicer):
	def create(self, request, response):
		#
		# リクエストの取得
		#
		element_dict = MessageToDict(request)

		#
		# 書式チェックの実施
		#
		try:
			jsonschema.validate(
				element_dict,
				create.schema,
				format_checker=jsonschema.FormatChecker()
			)
		#
		# JSON内のデータ書式に問題がある場合
		#
		except jsonschema.ValidationError as e:
			return OKResponse(ok = False, error = e)

		#
		# DB へ 登録
		#
		print('OK')
		session = SessionFactory.createSession()
		application = Application(**element_dict)
		session.add(application)
		session.commit()

		#
		# 成功時の処理
		#
		return OKResponse(ok = True)

