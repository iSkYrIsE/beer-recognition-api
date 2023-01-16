#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


from flask_restx import Api


api = Api(version='1.0',
		  title='mhs-models-api',
		  description="API for serving models developed for MHS sensorization API.")