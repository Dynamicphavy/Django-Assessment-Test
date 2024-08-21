from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def website(request):
    return render(request, 'about.html')