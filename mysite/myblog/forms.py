from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from myblog.models import Artical


# class ArticalForm(forms.Form):
#     content = forms.CharField(widget=SummernoteWidget())

class ArticalForm(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget())