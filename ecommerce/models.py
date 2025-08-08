from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

# ADMIN_ITEMS
class admin_items(models.Model):
    name_items = models.CharField(max_length=100)
    price_items = models.IntegerField()
    
    def __str__(self):
        return self.name_items
    
# CREATE USER
class user_create(models.Model):
    id_user = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    number = models.IntegerField()

    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    