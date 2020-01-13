from a3.grpc.service.application import ApplicationService
from a3.grpc.interface.application_pb2_grpc import add_ApplicationServicer_to_server

import time
import grpc
from concurrent import futures

if __name__ == '__main__':
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	add_ApplicationServicer_to_server(
		ApplicationService(), server)
	server.add_insecure_port('[::]:8080')
	server.start()
	try:
		while True:
			time.sleep(86400)
	except KeyboardInterrupt:
		server.stop(0)

