from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from sqlalchemy.sql.functions import user

from .models import *
from .serializers import *
from .forms import BidForm

# level0 - Начальник цеха
# level1 - Мастер участка
# level2 - Начальник ремонтной службы
# level3 - Ремонтный рабочий

def is_level0(user):
    return user.groups.filter(name='level2').exists()

def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['group1', 'group2']).exists()
# @login_required
# @user_passes_test(is_level0)
# or @user_passes_test(is_in_multiple_groups)
from django.contrib.auth.decorators import login_required, user_passes_test

class HomeView(View):

    def get(self, request):
        machine = Machine.objects.all()
        machine_status = MachineStatus.objects.all()
        feature = FeatureMachine.objects.all()
        context = {'machines': machine, 'features' : feature,
                   'machine_statuses': machine_status, }
        return render(request, 'main/home.html', context)

class BidView(View):

    def post(self, request):
        form = BidForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form = form.save(commit=False)
            form.sender = request.user.username
            form.save()

        return redirect("/home/bid/")

    def get(self, request):
        form = BidForm()
        end_bid = RequestStatus.objects.filter(status='Завершен')
        current_bid = RequestStatus.objects.filter(status='Ремонт')
        new_bid = RequestStatus.objects.filter(status='Ожидание')
        bid = RequestStatus.objects.all()

        context = {'statuses': status, 'end_bids': end_bid,
                   'bids': bid, 'new_bids': new_bid,
                   "form": form, "current_bids": current_bid}
        return render(request, 'main/bid.html', context)

class ContactView(View):
    def get(self, request):
        employee = Employee.objects.all()
        context = {'employees': employee}
        return render(request, 'main/contact.html', context)

class PositionViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin):

    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def create(self, request, *args, **kwargs):
        super(PositionViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class SpecialtyViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin):

    serializer_class = SpecialitySerializer
    queryset = Specialty.objects.all()

    def create(self, request, *args, **kwargs):
        super(SpecialtyViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class TypeRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin):

    serializer_class = TypeRequestSerializer
    queryset = TypeRequest.objects.all()

    def create(self, request, *args, **kwargs):
        super(TypeRequestViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)