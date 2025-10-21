from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 160)
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea)