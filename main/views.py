from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from .models import *
from .serializers import *
from .forms import BidForm



class MainView(View):

    def get(self, request):

        bid = Request.objects.all()
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine = Machine.objects.all()
        machine_status = MachineStatus.objects.all()
        specialist = Employee.objects.all()
        workplace = Workplace.objects.all()

        context = {'bids': bid, 'repairs': repair,
                   'workers': worker, 'machines': machine, 'specialists': specialist,
                   'machine_statuses': machine_status, 'workplaces': workplace}
        return render(request, 'main/home.html', context)


class ForemanHomeView(View):

    def get(self, request):

        bid = Request.objects.all()
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine = Machine.objects.all()
        machine_status = MachineStatus.objects.all()

        context = {'bids': bid, 'repairs': repair,
                   'workers': worker, 'machines': machine,
                   'machine_statuses': machine_status}
        return render(request, 'main/foreman_home.html', context)

class ForemanBidView(View):
    def get(self, request):
        end_bid = Request.objects.filter(status__requestStatus='Завершен')
        bid = Request.objects.filter(status__requestStatus='Ремонт')
        new_bid = Request.objects.filter(status__requestStatus='Ожидание')
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine_status = MachineStatus.objects.all()
        sender = Employee.objects.all()
        type = TypeRequest.objects.all()
        manufacture = Manufacture.objects.all()
        machine = Machine.objects.all()
        malfunction = Malfunction.objects.all()
        status = RequestStatus.objects.all()
        workplace = Workplace.objects.all()
        context = {'senders': sender, 'types': type,
                   'manufactures': manufacture, 'machines': machine,
                   'malfunctions': malfunction, 'statuses': status,
                   'end_bids': end_bid, 'bids': bid, 'repairs': repair,
                   'workers': worker, 'new_bids': new_bid, 'workplaces': workplace,
                   'machine_statuses': machine_status}
        return render(request, 'main/foreman_bid.html', context)

class RepairManView(View):
    def get(self, request):
        new_bid = Request.objects.filter(status__requestStatus='Ожидание')
        bid = Request.objects.filter(status__requestStatus='Ремонт')
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine_status = MachineStatus.objects.all()
        sender = Employee.objects.all()
        type = TypeRequest.objects.all()
        manufacture = Manufacture.objects.all()
        machine = Machine.objects.all()
        malfunction = Malfunction.objects.all()
        status = RequestStatus.objects.all()
        workplace = Workplace.objects.all()
        context = {'senders': sender, 'types': type,
                   'manufactures': manufacture, 'machines': machine,
                   'malfunctions': malfunction, 'statuses': status,
                   'new_bids': new_bid, 'bids': bid, 'repairs': repair,
                   'workers': worker, 'workplaces': workplace,
                   'machine_statuses': machine_status}

        return render(request, 'main/repairman.html', context)

class ContactView(View):
    def get(self, request):
        specialist = Employee.objects.all()

        context = {'specialists': specialist}
        return render(request, 'main/contact.html', context)

class BidView(View):

    def post(self, request):
        form = BidForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.status = RequestStatus.objects.get(id=1);
            form.save()
        return redirect("../main/bid.html")

    def get(self, request):
        bid = Request.objects.all()
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine_status = MachineStatus.objects.all()
        sender = Employee.objects.all()
        type = TypeRequest.objects.all()
        manufacture = Manufacture.objects.all()
        machine = Machine.objects.all()
        malfunction = Malfunction.objects.all()
        status = RequestStatus.objects.all()
        workplace = Workplace.objects.all()

        form = BidForm()

        context = {'senders': sender, 'types': type,
                   'manufactures': manufacture, 'machines': machine,
                   'malfunctions': malfunction, 'statuses': status,
                   'form': form, 'bids': bid, 'repairs': repair,
                   'workers': worker, 'workplaces': workplace,
                   'machine_statuses': machine_status}

        return render(request, 'main/bid.html', context)



class HRSHomeView(View):
    def get(self, request):

        bid = Request.objects.all()
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine = Machine.objects.all()
        machine_status = MachineStatus.objects.all()

        context = {'bids': bid, 'repairs': repair,
                   'workers': worker, 'machines': machine,
                   'machine_statuses': machine_status}
        return render(request, 'main/HRS_home.html', context)

class HRSBidView(View):
    def get(self, request):

        bid = Request.objects.all()
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine = Machine.objects.all()
        machine_status = MachineStatus.objects.all()

        context = {'bids': bid, 'repairs': repair,
                   'workers': worker, 'machines': machine,
                   'machine_statuses': machine_status}
        return render(request, 'main/HRS_bid.html', context)


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