#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


from flask_restx import fields

from beer_recognition_api.api.v1 import api


beer_recognition_input_model = api.model('BeerDetectionInput', {
	'picture': fields.String(description="File used to detect the beer type", required=True)
}, description="Input model for prediction.")


beer_recognition_output_model = api.model('BeerDetectionOutput', {
	'beer_type': fields.String(description="Predicted beer type. This can be Mahou, Alambra or 1906.", required=True, example='MAHOU')
}, description="Prediction output.")