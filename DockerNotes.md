## What is a Docker?
Docker is a containerized platform, it helps developers packages like application code, libraries, dependencies, configuration into a single unit called a container.

## Why Docker is Used?
Application may run on one system but fail on another, docker solves this by creating a consistent environment.

## Main Components of Docker?
1. Dockerfile --> Instruction to build image.
2. DockerImage --> It is a blueprint or template.
3. DockerContainer --> Running instance of image.
4. DockerHub --> Public Image Registry

## What is Amazon EC2?
EC2 is avirtual server on AWS, we can install software, host applications, deploy websites, Run docker containers.

## What is Amazon ECR?
ECR Stands for Elastic Container Registry, it is AWS private docker image storage service. It stores docker images securely.

## Why ECR is used?
When deploying apps to AWS we first create docker image, then we will store images in ECR, then EC2, ECS or EKS pull images from ECR.