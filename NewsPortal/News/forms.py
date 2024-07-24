from django import forms
from .models import Post
class NewsForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title', 'category', 'text', 'author']


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'text', 'author']


