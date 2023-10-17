from django.shortcuts import render
from django.http import HttpResponse

projectList=[
    {
        "id":"1",
        "title":"Website",
        "description":"Full Functional Website"
    },
    {
        "id":"2",
        "title":"App",
        "description":"Full Functional App"
    },
    {
        "id":"3",
        "title":"Software",
        "description":"Full Functional Software"
    }
]

def projects(request):
    msg="You're in the HomePage"
    number =12
    context={"message":msg,"number":number,"project":projectList}
    return render(request, 'project/project.html',context)

def project(request,id):
    projectObj=None
    for i in projectList:
        if i["id"] == id:
            projectObj=i
    context={"project":projectObj}
    return render(request, 'project/single-project.html',context)
