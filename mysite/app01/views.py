from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('app01.home')

# def news(request,nid1,nid2):
#     nid = nid1 + nid2
#     return HttpResponse(nid)

def page(request,n1,n2):
    nid = n1 + n2
    return HttpResponse(nid)