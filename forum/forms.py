from django import forms
from .models import Topic,Post



class TopicForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = ['title','description',]
        widgets = {
            'title':forms.TextInput(),
            'description':forms.Textarea()
        }



class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['content']
        widgets = {
            'content':forms.Textarea()
        }