from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        "active" : "index"
    }
    return render(request,"index.html",data)

def getLink(request):
    data = {
        "active" : "link"
    }
    return render(request,"upload_link.html",data)