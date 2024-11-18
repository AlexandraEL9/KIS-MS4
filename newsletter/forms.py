from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Name',
            'email': 'Email',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs['aria-label'] = 'Name'
        self.fields['email'].widget.attrs['aria-label'] = 'Email'

        for field in self.fields:
            placeholder = placeholders.get(field, '')
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False

