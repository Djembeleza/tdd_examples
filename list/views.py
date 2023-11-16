from django.shortcuts import render, redirect

from .models import (Item,List)



def home_page(request):
    return render(request, "home.html")

def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect("/lists/{0}/".format(nulist.id))

def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    return render(request, 'list.html', {"list": our_list})

def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=our_list)
    return redirect('/lists/{0}/'.format(our_list.id))