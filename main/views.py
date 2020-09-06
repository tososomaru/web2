import datetime as datetime
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import *
from .forms import BidForm
from predictive.models import Maint

class DashBoard(View):

    def pivot_data(request):
        dataset = Maint.objects.all()
        data = serializers.serialize('json', dataset)
        return JsonResponse(data, safe=False)

    def post(self, request):
        form = BidForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.status = RequestStatus.objects.get(id=1);
            form.save()
        return redirect("../main/dashboard.html")

    def get(self, request):

        sender = Employee.objects.all()
        type = TypeRequest.objects.all()
        manufacture = Manufacture.objects.all()
        machine = Machine.objects.all()
        malfunction = Malfunction.objects.all()
        status = RequestStatus.objects.all()
        form = BidForm()

        context = {'senders': sender, 'types': type,
                   'manufactures': manufacture, 'machines': machine,
                   'malfunctions': malfunction, 'statuses': status,
                   'form': form}


        return render(request, 'main/dashboard.html', context)


class MainView(View):
    def get(self, request):

        bid = Request.objects.all()
        repair = Repair.objects.all()
        worker = Employee.objects.only('Ремонтный рабочий')
        machine = Machine.objects.all()
        machine_status = MachineStatus.objects.all()

        context = {'bids': bid, 'repairs': repair,
                   'workers': worker, 'machines': machine,
                   'machine_statuses': machine_status}
        return render(request, 'main/home.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class BidView(View):

    def pivot_data(request):
        dataset = Main.objects.all()
        data = serializers.serialize('json', dataset)
        return JsonResponse(data, safe=False)

    def post(self, request):
        form = BidForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.status = RequestStatus.objects.get(id=1);
            form.save()
        return redirect("../main/bid.html")

    def get(self, request):

        sender = Employee.objects.all()
        type = TypeRequest.objects.all()
        manufacture = Manufacture.objects.all()
        machine = Machine.objects.all()
        malfunction = Malfunction.objects.all()
        status = RequestStatus.objects.all()
        form = BidForm()

        context = {'senders': sender, 'types': type,
                   'manufactures': manufacture, 'machines': machine,
                   'malfunctions': malfunction, 'statuses': status,
                   'form': form}

        return render(request, 'main/bid.html', context)




# class BidCreate(CreateView):
#     model = Request
#     form_class = BidForm
#     template_name = 'main/bid.html'
#     fields = ['typeRequest', 'manufacture']
#
# class BidUpdate(UpdateView):
#     model = Request
#     fields = ['typeRequest', 'manufacture']

