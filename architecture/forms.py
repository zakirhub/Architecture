from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ['name', 'email', 'phone', 'message']