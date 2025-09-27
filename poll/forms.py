from poll.models import Poll,PollOption
from django import forms
from django.forms import inlineformset_factory


class PollForm(forms.ModelForm):
    class Meta():
        model = Poll
        fields = ['title','description',]
        widgets = {
            'title':forms.TextInput(),
            'description':forms.Textarea()
        }

poll_option_set = inlineformset_factory(Poll,PollOption,fields=['text'],extra=3,can_delete=False,widgets={'text':forms.TextInput})


class PollOptionSet(poll_option_set):
    def clean(self):
        super().clean()
        
        field_forms = []

        if self.is_valid():
            for form in self.forms:
                if form.cleaned_data.get('text'):
                    field_forms.append(form) 

            if len(field_forms) < 2:
                raise forms.ValidationError('потрiбно мiнiмум два варiанта')
       



