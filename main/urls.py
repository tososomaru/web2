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
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/contact/', views.ContactView.as_view(), name='contact'),
    path("api/v2/", include(router.urls), name='apimain'),
    path('home/bid/', views.BidView.as_view(), name='bid'),
]

