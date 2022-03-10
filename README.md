# docker_opencv_python_sample

## What is included
- Opencv is built into the docker container
- Example user input

## Steps to build
chmod +x main.py

sudo docker build -t opencv-test .


## How to run

sudo docker run -it --rm  opencv-test [name]

example: sudo docker run -it --rm  opencv-test Gihan