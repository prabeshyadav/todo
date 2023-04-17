from django import forms
from django.forms import ModelForm
from .models import *

class taskForm(forms.ModelForm):
    class meta:
        model = task
        fields ='_all_'