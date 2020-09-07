from django.test import TestCase

from .ml_algorithm import ModelLSTM

import pandas as pd
import os
from os.path import normpath, join

#python manage.py test predictive.tests

class MLTests(TestCase):
    def test_algorithm(self):
        path_to_data = normpath(join(os.getcwd(), 'data/PM_test.txt'))
        data = pd.read_csv(path_to_data)
        model = ModelLSTM('ml_model/model_lstm.h5', 'ml_model/min_max_scaler.pkl')
        response = model.compute_prediction(data)
        return response
