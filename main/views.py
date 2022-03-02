from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DataEntryItems
from .forms import CreateNewList
# Create your views here.

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            cleanName = form.cleaned_data["name"]
            cleanAge = form.cleaned_data["age"]
            cleanTitle = form.cleaned_data["title"]
            cleanHometown = form.cleaned_data["hometown"]
            newDataItems = DataEntryItems(name=cleanName, age=cleanAge, title=cleanTitle, hometown=cleanHometown)
            newDataItems.save()

        return HttpResponseRedirect("/confirmation/%i" % newDataItems.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def confirmation(response, id):
    CurrentDataItem = DataEntryItems.objects.get(id=id)
    DataList = DataEntryItems.objects.all()
    return render(response, "main/confirmation.html", {"CurrentDataItem": CurrentDataItem, "DataList": DataList} )



