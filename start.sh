#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -P \
  --name=${app} \
  -v $PWD:/app ${app}