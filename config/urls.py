"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from predictive.urls import urlpatterns as predictive_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'main/', include('main.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    url('dashboard/', include('dashboard.urls'))
]

urlpatterns+= predictive_urlpatterns
