from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'myapp/index.html', {'items': items})

def item(request):
    return HttpResponse("ITEM PAGE")

def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'myapp/detail.html', {'item': item})


def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
        
    return render(request, 'myapp/item-form.html', {'form': form})


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
        
    return render(request, 'myapp/item-form.html', {'form': form})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('myapp:index')
    
    return render(request, 'myapp/item-delete.html', {'item': item})