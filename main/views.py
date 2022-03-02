from django.shortcuts import render
from django.http import HttpResponse
from .models import DataEntryList, Item
# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def confirmation(response, id):
    DataList = DataEntryList.objects.get(id=2)
    ItemList = DataList.item_set.get(id=id)
    return render(response, "main/confirmation.html", {"DataList": DataList, "ItemList":ItemList})



# def item(response, id):
#     DataList = DataEntryList.objects.get(id=id)
#     ItemList = DataList.item_set.get(id=id)
#     #return HttpResponse("<h1>we are talking about dataListName: %s  and itemListName: %s</h1>" % (str(DataList.name), str(ItemList.name)))
#     return render(response, "main/item.html", {"itemListName":str(ItemList.name), "itemListAge":ItemList.age, "itemListTitle":str(ItemList.title), "itemListTitle":str(ItemList.hometown) })
