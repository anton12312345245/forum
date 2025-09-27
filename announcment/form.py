from announcment.models import Announcment
from django import forms
from django.forms import inlineformset_factory


class AnnouncmentForm(forms.ModelForm):
    class Meta():
        model = Announcment
        fields = ['title','text',]
        widgets = {
            'title':forms.TextInput(),
            'text':forms.Textarea()
        }

