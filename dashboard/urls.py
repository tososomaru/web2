from django.conf.urls import url
from .views import DashBoard, PredictiveBoard
from . import dashboard_dash
from . import predictive_dach

urlpatterns = [
    url(r'^$', DashBoard.as_view(), name='dashboard'),
    url(r'predictive', PredictiveBoard.as_view(), name='predictive'),
]
