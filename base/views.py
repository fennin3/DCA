from django.shortcuts import render



def home(request):
    return render(request, "base/index.html")


def about(request):
    return render(request, 'base/about.html')


def services(request):
    return render(request, 'base/services.html')


def contact(request):
    return render(request, 'base/contact.html')