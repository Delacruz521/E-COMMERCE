from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .otp import *
from .models import *
from .forms import *
from django.conf import settings 

# payment
# import stripe

# smtp
from django.core.mail import send_mail

from django.contrib.auth import login
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# login for
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            try:
                user = user_create.objects.get(username=username, password=password)
                request.session.flush()
                request.session["id_user"] = user.id_user
                print("success login")
                return redirect(home)
            except user_create.DoesNotExist:
                messages.error(request, "INVALID")
    return render(request, 'login.html')
 
def  create_account(request):
    if request.method == "POST":
        form = account(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)
        else:
            messages.error(request, "INVALID")
    else:
        form = account()
    return render(request, 'create_account.html', {'form': form})

# dashboard
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

#smtp
def message_email(request):
    if request.method == 'POST':
        subject = request.POST["subject"]
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        send_mail(
            subject,
            f"Name {name} \n\n Email: <{email}> \n\n {message}",
            from_email='settings.EMAIL_HOST_USER',
            recipient_list=["karlanthony521@gmail.com"],
            fail_silently=False, 
        )
    else:
        print("not sending")
    return render(request, 'home.html', {})


# def payment_method(request):
#     try:
#         intent = stripe.PaymentIntent.create(
#             amount = 2000,
#             currency = 'usd',
#             payment_method_types = ['card'],
#         )
#         return JsonResponse({'clientSecret': intent['client_secret']})
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=403)