#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


from flask_restx import reqparse, inputs
from werkzeug.datastructures import FileStorage


beer_recognition_parser = reqparse.RequestParser()
beer_recognition_parser.add_argument('picture', location='files', type=FileStorage, required=True)
