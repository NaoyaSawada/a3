build:
	python -m grpc_tools.protoc -I ./protocol/ --python_out=./interface/ --grpc_python_out=./interface/ application.proto response.proto

clean:
	rm ./interface/[a-z]*.py

