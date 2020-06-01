from django import forms
from .models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'post']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'col-md-7 form-control'}),
            'post': forms.Textarea(attrs={'placeholder': 'Write you\'r Article!',
                                          'class': 'col-md-7 form-control h-100 mt-3'})}




