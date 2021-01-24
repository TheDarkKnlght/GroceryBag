from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('cart')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	# return render (request=request, template_name="main/register.html", context={"register_form":form})
	return render (request, 'main/register.html', {"register_form" : form})

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
    # item = Item.objects.get(id=id)
    # if request.method == "POST" :
    #     form = ItemForm(request.POST, item)
    #     if form.is_valid():
    #         # item.delete()
    #         form.save()
    #         return redirect('home')
    # else :
    #     form = ItemForm(item)
    #     return render(request, 'cart/update.html', {'form': form})
    item = Item.objects.get(id=id)
    return render(request, 'cart/update.html', {'item': item})