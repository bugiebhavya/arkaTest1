from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200,default='India')
    def __str__(self): 
        return self.company_name 

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_id = models.CharField(max_length=30,primary_key = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.IntegerField()
    color = models.CharField(max_length=30)
    created_date = models.DateTimeField('date created')
    def __str__(self): 
        return self.product_name 

