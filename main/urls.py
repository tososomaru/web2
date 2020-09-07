from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PositionViewSet, SpecialtyViewSet, TypeRequestViewSet
from . import views
from django.conf.urls import url


router = DefaultRouter(trailing_slash=False)
router.register(r"position", PositionViewSet, basename="position")
router.register(r"specialty", SpecialtyViewSet , basename="specialty")
router.register(r"typerequest", TypeRequestViewSet, basename="typerequest")

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='home'),
    url(r'about', views.AboutView.as_view(), name='about'),
    url(r'bid', views.BidView.as_view(), name='bid'),
    url(r"^api/v1/", include(router.urls))
]

