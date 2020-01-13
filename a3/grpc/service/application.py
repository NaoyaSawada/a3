from a3.grpc.interface.application_pb2 import *
from a3.grpc.interface.application_pb2_grpc import ApplicationServicer

class ApplicationService(ApplicationServicer):
	def create(self, request, response):
		print(self, request, response)
		return ApplicationCreateRequest(
			name = 'SAWADA'
		)

