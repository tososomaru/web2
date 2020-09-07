import inspect
from predictive.ml_algorithm import ModelLSTM
from predictive.models import *


class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, endpoint_name, algorithm_object, algorithm_name,
                      algorithm_status, algorithm_version, owner,
                      algorithm_description, algorithm_code) -> object:
        # get endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)

        # get algorithm
        database_object, algorithm_created = MLAlgorithm.objects.get_or_create(
            name=algorithm_name,
            description=algorithm_description,
            code=algorithm_code,
            version=algorithm_version,
            owner=owner,
            parent_endpoint=endpoint)

        if algorithm_created:
            status = MLAlgorithmStatus(status=algorithm_status,
                                       created_by=owner,
                                       parent_mlalgorithm=database_object,
                                       active=True)
            status.save()

        # add to registry
        self.endpoints[database_object.id] = algorithm_object


def deploy_algorithm():
    try:
        registry = MLRegistry()
        rf = ModelLSTM()
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
        print("Исключение при загрузке алгоритма в реестр", str(e))
