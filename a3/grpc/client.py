from a3.grpc.interface.application_pb2 import *
from a3.grpc.interface.application_pb2_grpc import ApplicationStub
import grpc

if __name__ == '__main__':
	with grpc.insecure_channel('localhost:2020') as channel:
		stub = ApplicationStub(channel)
		print(stub.create(ApplicationCreateRequest(
			name = 'SAWADA'
		)))

