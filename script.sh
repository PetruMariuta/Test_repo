#!/bin/bash

IMAGE_NAME=myapp
CONTAINER_NAME=myapp_container
CONTAINER_PORT=8000
REGISTRY_URL=your-registry-url.com
REGISTRY_USERNAME=username
REGISTRY_PASSWORD=password


docker build -t $IMAGE_NAME .


docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME


docker login -u $REGISTRY_USERNAME -p $REGISTRY_PASSWORD $REGISTRY_URL
docker push $REGISTRY_URL/$IMAGE_NAME


docker stop -f $CONTAINER_NAME
docker rm -f $CONTAINER_NAME

docker run -d --name $CONTAINER_NAME -p $CONTAINER_PORT:$CONTAINER_PORT $REGISTRY_URL/$IMAGE_NAME

sleep 25

curl -I http://localhost:$CONTAINER_PORT/liveness

echo "start k8s deployment"

kubectl apply -f myapp.yml
kubectl get deployments
kubectl get services

