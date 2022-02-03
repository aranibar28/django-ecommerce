from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='productos', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    def __str__(self):
        return self.title

class Client(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    direction = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.phone