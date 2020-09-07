from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views
from django.conf.urls import url


router = DefaultRouter(trailing_slash=False)
router.register(r"position", PositionViewSet, basename="position")
router.register(r"specialty", SpecialtyViewSet , basename="specialty")
router.register(r"typerequest", TypeRequestViewSet, basename="typerequest")

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('head/', views.MainView.as_view(), name='head_place'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('head/bid/', views.BidView.as_view(), name='bid'),
    path("api/v1/", include(router.urls)),
    path('repairman/', views.RepairManView.as_view(), name='repairman'),
    path('headrepair/', views.HRSHomeView.as_view(), name='head_repair_service_home'),
    path('headrepair/bid/', views.HRSBidView.as_view(), name='head_repair_service_bid'),
    path('foreman/', views.ForemanHomeView.as_view(), name='foreman_home'),
    path('foreman/bids/', views.ForemanBidView.as_view(), name='foreman_bids'),
]

