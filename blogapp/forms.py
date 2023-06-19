from django import forms
# from django.forms import ModelForm
from froala_editor.widgets import FroalaEditor
from .models import *
class Blogform(forms.ModelForm):
    class Meta:
        model = Blogmodel
        fields = ['content']


