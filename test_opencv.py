#!/usr/bin/env python
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Name of person to greet")

args = parser.parse_args()

print(f"Hi, {args.name}!")

img = cv2.imread('docker_python.jpg',1)

print("Successfully loaded opencv-python!")



