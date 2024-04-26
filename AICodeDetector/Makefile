
docker build:
	docker build -t detector .

curdir := $(shell pwd)
docker run:
	docker run -it --gpus all -v curdir:/work detector
