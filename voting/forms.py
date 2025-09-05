from voting.models import Vote
from django import forms

class VoteForm(forms.ModelForm):
    class Meta():
        model = Vote
        fields = ['title','description']
        widgets = {
            'title':forms.TextInput(),
            'description':forms.Textarea()
        }




