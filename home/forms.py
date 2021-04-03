from django import forms
from .models import Post, Catergory

choices = Catergory.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'author','category','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter title here'}),
            #'author': forms.Select(attrs={'class': 'form-control'})
            'author': forms.TextInput(attrs={'class': 'form-control','value':'' , 'id' : 'user','type':'hidden'}),
            'catergory': forms.Select(choices='choice_list',attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
          
        } 




