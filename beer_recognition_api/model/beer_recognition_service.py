#!/usr/bin/python3
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


import os
import keras
import numpy as np
from PIL import Image
from typing import Any, Dict, Tuple
from werkzeug.datastructures import FileStorage


from beer_recognition_api import logger


class BeerRecognitionService:
    """Loads the model and perform predictions over it.

    Also maps results of the model
    """

    def __init__(self, model_path: str) -> None:
        """
        Args:
            model_path: the path of the pickle file where model is located
        """

        self.model = self._load_model(model_path=model_path)

    def _load_model(self
        , model_path: str
    ) -> None:
        """Loads the model into memory

        Args:
            model_path: the file system path where model is located

        Returns:
            the model path
        """

        logger.info('loading model')

        model = keras.models.load_model(model_path)

        logger.info('model loaded sucessfully')

        return model

    def _map_categories(self
        , model_output: int
    ) -> str:
        """Maps the categories between the model output (int) and the desired result (str)

        Args:
            model_output: the output of the model

        Returns:
            the output
        """

        mappings = {
            0: 'alambra'
            , 1: 'coronita'
            , 2: 'mahou'
        }

        if model_output not in mappings:
            logger.warning(f'trying to map model output with value of {model_output}')
            raise ValueError('The model output does not fit within the available mappings')

        mapping = mappings[model_output]

        return mapping

    def classify(self
        , picture: FileStorage
    ) -> str:
        """Predicts the beer type

        Args:
            picture: the picture containing a beer

        Returns:
            the picture type, beign suitable mahou, alambra or coronita
        """

        logger.info('loading image')

        # load image with pillow and transform it into an array
        img = Image.open(picture).resize((150, 150))
        img_data = np.asarray(img)
        img_data = np.expand_dims(img_data, axis=0)

        logger.info('applying model')

        # apply model
        model_output = self.model.predict(img_data)

        logger.debug(f'resulting model {model_output}')
        logger.info('mapping categories')

        # map categories
        model_output = np.argmax(model_output)
        result = self._map_categories(model_output=model_output)

        logger.info('prediction finished successfully')

        return result