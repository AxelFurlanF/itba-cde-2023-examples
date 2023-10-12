.PHONY: build run

# Name of your docker image
IMAGE_NAME=my-python-app

# Port to which the server binds inside Docker
DOCKER_PORT=80

# Port to which you want to map the binding on your host machine
HOST_PORT=4000

build:
	@docker build -t $(IMAGE_NAME) .

run:
	@docker run -p $(HOST_PORT):$(DOCKER_PORT) $(IMAGE_NAME)

enter-container:
	@docker run -it $(IMAGE_NAME) /bin/bash
