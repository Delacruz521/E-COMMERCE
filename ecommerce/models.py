from django.db import models

# Create your models here.

# ADMIN_ITEMS
class admin_items(models.Model):
    name_items = models.CharField(max_length=100)
    price_items = models.IntegerField()
    
    def __str__(self):
        return self.name_items
    
# CREATE USER
class user_create(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
