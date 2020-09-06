from django.test import TestCase

from predictive.XGBClassifier import ModelClassifier

#python manage.py test predictive.tests

class MLTests():
    def test_algorithm(self):
        input_data = {
            "voltmean_3h":  	180.133784 	,
            "rotatemean_3h": 440.60832 	,
            "pressuremean_3h": 94.137969,
            "vibrationmean_3h ": 41.551544 	,
            "voltsd_3h": 21.322735 	,
            "rotatesd_3h": 48.770512,
            "pressuresd_3h": 2.135684,
            "vibrationsd_3h": 10.037208,
            "voltmean_24h": 169.733809,
            "rotatemean_24h": 445.179865 	,
            "pressuremean_24h": 96.797113 ,
            "vibrationmean_24h": 40.38516 ,
            "voltsd_24h": 11.23312,
            "rotatesd_24h": 48.717395,
            "pressuresd_24h": 10.07988 	,
            "vibrationsd_24h":5.853209 	,
            "error1count": 0.0,
            'error2count' : 0.0,
            'error3count': 0.0,
            'error4count': 0.0,
            'error5count': 0.0,
            'comp1': 20.0,
            'comp2': 215.0,
            'comp3': 155.0 	,
            'comp4 	': 170.0,
            'age': 18,
            "model1": 0.0,
            "model2": 0.0,
            "model3": 1.0,
            "model4": 0.0,
        }
        model = ModelClassifier()
        response = model.compute_prediction(input_data)
        print(response)
        return response

a = MLTests().test_algorithm()