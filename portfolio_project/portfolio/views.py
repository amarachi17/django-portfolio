from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Project
from .forms import ContactForm
from django.conf import settings 

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'projects': projects})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        full_message = f"""
        New message from your portfolio site:
        Name: {name}
        Email: {email}

        Message: {message} """

        send_mail(
            subject = f'Porfolio Message from {name}',
            message= full_message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.EMAIL_HOST_USER],
            fail_silently = False,
        )
        return render(request, "contact.html", {"form": ContactForm(), "success":True})
    return render(request, 'contact.html', {'form': form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    return render(request, "project_detail.html", {"project": project, "images": images})