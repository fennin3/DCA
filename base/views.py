from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
from .utils import sending_mail


def home(request):
    services = models.Service.objects.all()
    testimonies = models.Testimony.objects.all()

    if(services.count() > 4):
        services = services[0:4]
    
    context = {
        "services":services,
        "testimonies":testimonies
    }
    return render(request, "base/index.html", context)

def about(request):
    return render(request, 'base/about.html')


def services(request):
    services = models.Service.objects.all()
    context = {
        "services":services,
    }
    return render(request, 'base/services.html', context)


def contact(request):
    return render(request, 'base/contact.html')


def subscribe(request):
    form = models.Email.objects.create(email=request.POST.get('email'))
    form.save()
    messages.success(request, "Subscription successful")
    return redirect('home')


def sendMessage(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    topic=request.POST.get("topic")
    message=request.POST.get("comment")

    tpc = f"DCA - {topic}"
    msg = '''Name Of Sender: \t {}\n\nEmail Of Sender: \t{}\n\nMESSAGE\n\n{}'''.format(name,email,message)
    sending_mail(msg,topic)
    messages.success(request, f"Thank you for reaching out to us, {name}. We will respond as soon as possible.")
    return redirect('home')
