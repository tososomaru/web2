from django import forms
from .models import *

class BidForm(forms.ModelForm):
    """Форма заявки"""
    attrs = {'class': 'custom-select'}
    sender = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    typeRequest  = forms.ModelChoiceField(queryset=TypeRequest.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    machine  = forms.ModelChoiceField(queryset=Machine.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    status  = forms.ModelChoiceField(queryset=RequestStatus.objects.all(),
                                    widget=forms.Select(attrs=attrs), required=False)
    class Meta:
        model = Request
        fields = ('sender', 'typeRequest', 'sender',
                  'machine', 'malfunction', 'status')




