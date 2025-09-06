from voting.models import Vote,VoteOption
from django import forms
from django.forms import inlineformset_factory


class VoteForm(forms.ModelForm):
    class Meta():
        model = Vote
        fields = ['title','description',]
        widgets = {
            'title':forms.TextInput(),
            'description':forms.Textarea()
        }

vote_option_set = inlineformset_factory(Vote,VoteOption,fields=['text'],extra=3,can_delete=False,widgets={'text':forms.TextInput})


class VoteOptionSet(vote_option_set):
    def clean(self):
        super().clean()
        
        field_forms = []

        if self.is_valid():
            for form in self.forms:
                if form.cleaned_data.get('text'):
                    field_forms.append(form) 

            if len(field_forms) < 2:
                raise forms.ValidationError('потрiбно мiнiмум два варiанта')
       



