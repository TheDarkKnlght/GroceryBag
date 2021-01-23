from django.shortcuts import render
from .models import Item

def post_list(request) :
    items = Item.objects.all()
    return render(request, 'cart/index.html', {'items': items})
