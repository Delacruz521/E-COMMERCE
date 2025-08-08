from django.shortcuts import render, redirect, get_object_or_404
from .otp import *
from .models import *
from .forms import *

def login(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def list_items(request):
    items = admin_items.objects.all()
    return render(request, 'admin_dashboard.html', {'items': items})

def add_items(request):
    if request.mehtod == 'POST':
        form = admin_items_forms(request.POST)
        if form.is_vallid():
            form.save()
        return redirect('admin_dashboard')
    else:
        form = admin_items_forms()
    return render(request, 'admin_dashboard.html')

def update_items(request, pk):
    items = get_object_or_404(admin_items, pk=pk)
    if request.method == 'POST':
        form = admin_items_forms(request.POST, instance=items)
        if form.is_valid():
            form.save()
        return redirect('admin_dashboard')
    else:
        form = admin_items_forms()
    return render(request, 'admin_dashboard.html', {'form': form})

def delete_items(request, pk):
    items = get_object_or_404(admin_items, pk=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('admin_dashboard')
    return render(request, 'admin_dashboard.html')  