from django.shortcuts import render


def index(request):
    context = {'nav': 'index'}
    return render(request, 'index.html', context)


def login(request):
    context = {'nav': 'login'}
    return render(request, 'login.html', context)


def register(request):
    context = {'nav': 'register'}
    return render(request, 'register.html', context)

# Create your views here.
