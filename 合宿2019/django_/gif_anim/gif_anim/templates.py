from django.http.response import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'teamF_webapp_01.html')