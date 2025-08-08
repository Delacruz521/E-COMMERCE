from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login_page'),

    # ADMIN 
    path('add/', add_items, name='add_items'),
    path('update/<int:pk>/', update_items, name='update_items'),
    path('delete/<int:pk>/', delete_items, name='delete_items'),

    # USER
    
    # DASHBOARD
    path('dashboards/', dashboard, name='dashboard'),
]
