from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def grocery_list(request) :
    items = Item.objects.all()
    return render(request, 'cart/index.html', {'items': items})

def home(request) :
    return render(request, 'main/home.html', {})

def add_entry(request) :
    if request.method == "POST" :
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = ItemForm()
        return render(request, 'cart/add.html', {'form': form})

def remove(request, id) : 
    item = Item.objects.get(id=id) 
    item.delete() 
    return redirect('home') 

def update(request, id) :
    item = Item.objects.get(id=id)
    