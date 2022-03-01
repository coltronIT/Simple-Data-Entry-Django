from django.shortcuts import render
from django.http import HttpResponse
from .models import DataEntryList, Item
# Create your views here.

def index(response):
    return HttpResponse("<h1>form</h1>")

def item(response, id):
    item = DataEntryList.objects.get(id=id)
    return HttpResponse("<h1>we are talking about itemName: %s</h1>" % item.name)

def confirmation(response):
    return HttpResponse("<h1>confirmation</h1>")