build:
	python -m grpc_tools.protoc -I ./protocol/ --python_out=./rpc/ --grpc_python_out=./rpc/ main.proto

clean:
	rm ./rpc/*.py

