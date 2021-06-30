from django import forms
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.forms import fields
from . models import edit_testimonials
from . models import edituser

class ImageForm(forms.ModelForm): 
    class Meta:
        model=edit_testimonials
        fields=("image","name","designation")

# class EdituserForm(forms.ModelForm):
#     status=(('opt1','Upgraded'),('opt2','Free'))
#     # accnt= forms.ChoiceField(choices=status,widget=forms.RadioSelect)
#     class Meta:
#         model=edituser
#         fields=("email_id","accnt")
        