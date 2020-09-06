from django.urls import path, include
from . import views
from django.conf.urls import url
from charts import django_plotly_dash
urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='home'),
    url(r'about', views.AboutView.as_view(), name='about'),
    url(r'bid', views.BidView.as_view(), name='bid'),
    url(r'dashboard', views.DashBoard.as_view(), name='dashboard')

]

