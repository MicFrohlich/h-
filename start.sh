#!/bin/bash
app="homeplus-exercise-michael-f"

docker build -t ${app} .
docker run -d -P \
  --name=${app} \
  -v $PWD:/app ${app}