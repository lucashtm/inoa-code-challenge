from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')

class Expense(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)