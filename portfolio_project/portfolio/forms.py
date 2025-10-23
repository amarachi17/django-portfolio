from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 160, required=True, label="Enter Your Name")
    email = forms.EmailField(required=True, label="Enter Your Email")
    message = forms.CharField(widget = forms.Textarea, required=True, label="Your Message")