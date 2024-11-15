
build:
	docker build -t detector -f AICodeDetector/Dockerfile ./AICodeDetector

run:
	docker run -it --gpus all -v /home/kato/AICodeDetectorWorkspace/AICodeDetector:/work detector

exec:
	docker exec -it focused_mahavira bash

ssh-to-sub:
	ssh kato@192.168.11.114

build-generator:
	docker build -t detectgpt -f DetectCodeGPT/Dockerfile ./DetectCodeGPT

run-generator:
	docker run -it --gpus all -v /home/kato/AICodeDetectorWorkspace/DetectCodeGPT:/work detectgpt
