from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html', {'password': 'rty67rjhvb87'})


def hello_fun(request):
    return HttpResponse('My name is Sergey...')
