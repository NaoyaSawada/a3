from rpc.app_pb2 import *
from rpc.app_pb2_grpc import ApplicationGatewayStub
import grpc

if __name__ == '__main__':
	with grpc.insecure_channel('localhost:8080') as channel:
		stub = ApplicationGatewayStub(channel)
		print(stub.create(AppComponent(
			name = 'SAWADA'
		)))

