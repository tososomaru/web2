from django.conf.urls import url
from .views import DashBoard
from . import django_plotly_dash

urlpatterns = [
    url(r'^$', DashBoard.as_view(), name='dashboard'),
]
