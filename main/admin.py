from django.contrib import admin
from .models import *
from data.models import *
from django.contrib.auth.models import User

admin.site.register(Machine)
admin.site.register(MachineStatus)
admin.site.register(Position)
admin.site.register(TypeRequest)
admin.site.register(Specialty)
admin.site.register(Malfunction)
admin.site.register(Manufacture)
admin.site.register(FeatureMachine)
admin.site.register(Employee)
admin.site.register(Repair)
admin.site.register(Request)
admin.site.register(RequestStatus)
admin.site.register(MachineCondition)
admin.site.register(Workplace)