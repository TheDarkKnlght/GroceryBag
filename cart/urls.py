from django.urls import path
from . import views

urlpatterns = [
    path('', views.grocery_list, name = 'home'),
    path('add', views.add_entry, name = 'add_entry'),
    path('del/<int:id>', views.remove, name="del"),
    path('update/<int:id>', views.update, name="update"),
]