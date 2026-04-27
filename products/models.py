from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True,blank=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    def __str__(self):
        return self.name
   