
from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widget = {
            "name" : TextInput(attrs={'class': 'form-control'}),
            "email": EmailInput(attrs={'class': 'form-control'}),
        }




