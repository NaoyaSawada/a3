import click
from flask import Flask

app = Flask(__name__)

#
# GRPCDの起動
#
def start_grpcd(host, port):
	import grpc
	from concurrent import futures

	#
	# サーバの作成
	#
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	#
	# サービスの登録
	#
	from a3.grpc.service.application import ApplicationService
	from a3.grpc.interface.application_pb2_grpc import add_ApplicationServicer_to_server
	add_ApplicationServicer_to_server(ApplicationService(), server)

	#
	# サーバの起動
	#
	server.add_insecure_port('%s:%d' %(host, port))
	server.start()

#
# HTTPDの起動
#
def start_httpd(host, port, debug):
	app.run(host = host, port = port, debug = debug)

@click.command()
@click.option('--host', default = '0.0.0.0')
@click.option('--http-port', default = 2019)
@click.option('--grpc-port', default = 2020)
@click.option('--debug', default = False)
def start_daemons(host, http_port, grpc_port, debug):
	#
	# GRPCDの起動
	#
	start_grpcd(host, grpc_port)

	#
	# HTTPDの起動
	#
	start_httpd(host, http_port, debug)

if __name__ == "__main__":
	start_daemons()

