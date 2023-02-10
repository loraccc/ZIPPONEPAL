from django import forms
from .models import destination

def contact_register(request):
    class Meta:
        fields=("name","email","phone")
        model=destination