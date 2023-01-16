#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


import os


# api config
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/beer-recognition/v1'
DEBUG_MODE = True

# model path config
MODEL_PATH = os.getenv('MODEL_PATH', default='./model')  