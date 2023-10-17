from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request, 'project/project.html')

def project(request,id):
    return render(request, 'project/single-project.html')
