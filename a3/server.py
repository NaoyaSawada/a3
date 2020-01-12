from rpc.app_pb2 import *
from rpc.app_pb2_grpc import add_ApplicationGatewayServicer_to_server, ApplicationGatewayServicer

import time
import grpc
from concurrent import futures

class ApplicationGatewayServicer(ApplicationGatewayServicer):
	def create(self, request, response):
		print(self, request, response)
		return AppComponent(
			name = 'SAWADA'
		)

if __name__ == '__main__':
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	add_ApplicationGatewayServicer_to_server(
		ApplicationGatewayServicer(), server)
	server.add_insecure_port('[::]:8080')
	server.start()
	try:
		while True:
			time.sleep(86400)
	except KeyboardInterrupt:
		server.stop(0)

