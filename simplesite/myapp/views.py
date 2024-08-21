from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def fleat(request):
    return render(request, "about.html")