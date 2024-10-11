from django import forms
from .models import Post



class NewsForm(forms.ModelForm):
    title = forms.CharField(min_length=15, widget=forms.Textarea({'cols': 70, 'rows': 2}))
    text = forms.CharField(min_length=150, widget=forms.Textarea({'cols': 70, 'rows': 7}))
    class Meta:
        model = Post
        fields = ['title', 'category', 'text', 'author']

class ArticlesForm(forms.ModelForm):
    title = forms.CharField(min_length=15, widget=forms.Textarea({'cols': 70, 'rows': 2}))
    text = forms.CharField(min_length=150, widget=forms.Textarea({'cols': 70, 'rows': 7}))
    class Meta:
        model = Post
        fields = ['title', 'category', 'text', 'author']


