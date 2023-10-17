from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request,'project.html')

def project(request,id):
    return HttpResponse('This is Our one Page'+' '+str(id))
