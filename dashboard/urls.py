from django.conf.urls import url
from .views import DashBoard, PredictiveBoard
from . import dashboard_dash
from . import predictive_dach
from django.urls import path
urlpatterns = [
    path('', DashBoard.as_view(), name='dashboard'),
    path('predictive', PredictiveBoard.as_view(), name='predictive'),
]
