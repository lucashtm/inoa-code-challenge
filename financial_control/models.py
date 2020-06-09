from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=20, decimal_places=10)