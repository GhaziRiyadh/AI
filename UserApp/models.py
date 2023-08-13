from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CatDog(models.Model):
    image = models.ImageField('images')
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    _password = models.TextField(name='password',db_column='password')
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "userapp_user"


class UserType(models.Model):
    class ChType(models.TextChoices):
        ADMIN = 'A'
        SELLER = 'S'
        BUYER = 'B'
    type = models.TextField(choices=ChType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class FinancialAccount(models.Model):
    numberOfAccount = models.IntegerField(unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
