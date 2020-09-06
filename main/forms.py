from django import forms
from .models import *

class BidForm(forms.ModelForm):
    """Форма заявки"""
    attrs = {'class': 'custom-select'}
    sender = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    type  = forms.ModelChoiceField(queryset=TypeRequest.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    manufacture  = forms.ModelChoiceField(queryset=Manufacture.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    machine  = forms.ModelChoiceField(queryset=Machine.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    malfunction  = forms.ModelChoiceField(queryset=Malfunction.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    status  = forms.ModelChoiceField(queryset=RequestStatus.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    class Meta:
        model = Request
        fields = ('sender', 'typeRequest', 'manufacture',
                  'machine', 'malfunction', 'status')



