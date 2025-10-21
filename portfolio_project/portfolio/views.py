from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Project
from .forms import ContactForm
from django.conf import settings 

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'projects': projects})

def contact(request):
    form = ContactForm(request.POST or none)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        send_mail(
            subject = f'Porfolio Message from {name}',
            message= f'From: {email}\n\n{message}',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.EMAIL_HOST_USER],
        )
        return redirect('home')
    return render(request, 'contact.html', {'form': form})
