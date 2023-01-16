#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


import flask
import datetime
import pandas as pd
from flask_restx import Resource


from beer_recognition_api.api.v1 import api
from beer_recognition_api.core import limiter
from beer_recognition_api import logger, config
from beer_recognition_api.utils import handle400error, handle404error, handle500error

from beer_recognition_api.api.beer_recognition_models import *
from beer_recognition_api.api.beer_recognition_parsers import *
from beer_recognition_api.model.beer_recognition_service import BeerRecognitionService


beer_recognition_ns = api.namespace('model', description='Beer recognition model')


service = BeerRecognitionService(model_path=config.MODEL_PATH)


@beer_recognition_ns.route('/predict')
class Predict(Resource):

    @api.expect(beer_recognition_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(beer_recognition_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour') 
    def post(self):
        """
        Returns the beer indicated in the attached file. The beer can be Mahou, Alambra or Coronita.
        """

        global service

        logger.info('new request arrived')

        # retrieve arguments
        obj = beer_recognition_parser.parse_args()
        picture = obj['picture']

        logger.info('performing model prediction')

        # build beer recommendation
        try:
            beer = service.classify(picture=picture)
        except Exception as e:
            logger.exception(f'Unknown error occurred {e}')
            return handle500error(beer_recognition_ns)

        # format results
        result = {
            'beer_type': beer.upper()
        }

        logger.info('request processed sucessfully')

        return result
