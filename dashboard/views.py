from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

class DashBoard(View):

    def get(self, request):
        return render(request, 'dashboard/dashboard.html')

class PredictiveBoard(View):

    def get(self, request):
        return render(request, 'dashboard/ml.html')