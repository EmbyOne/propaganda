from django.db import models  
from django.forms import fields  
from .models import messageModel
from django import forms

class messageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = messageModel
        # It includes all the fields of model  
        fields = '__all__' 
