"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


# ML registry
import inspect
from web2.predictive.registry import MLRegistry
from web2.predictive.ml_algorithm import ModelLSTM



try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = ModelLSTM()
    # add to ML registry
    registry.add_algorithm(endpoint_name="binary classification models",
                            algorithm_object=rf,
                            algorithm_name="model LSTM",
                            algorithm_status="test",
                            algorithm_version="0.0.1",
                            owner="Nikita",
                            algorithm_description="Предскажет, выйдет ли оборудование из строя в течение"
                                                  " определенного периода времени (30 циклов).",
                            algorithm_code=inspect.getsource(ModelLSTM))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))

print('test')