from django import forms
from django.forms import ModelForm
from .models import Post
class PostForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(max_length=2000, widget = forms.Textarea())

class PostForm2(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']

