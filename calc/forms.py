from django import forms

class name_form(forms.Form):
    your_name = forms.CharField(label='Enter pokaemon character', max_length=100)