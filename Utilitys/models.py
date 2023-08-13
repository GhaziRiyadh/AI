from django.utils import timezone
from django.db import models
from UserApp.models import User 


from Product.models import Providers, WhereHouses
# Create your models here.


# class models.Model(models.Model):
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    path = models.ImageField('files/images')
    user = models.ForeignKey(
        User,
        related_name='user_image',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# class Description(models.Model):
#     desc_ar = models.TextField()
#     desc_en = models.TextField()
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)


class PhoneNumber(models.Model):
    phone = models.IntegerField()
    user = models.ForeignKey(
        User,
        related_name='user_phone',
        on_delete=models.CASCADE
    )
    providers = models.ForeignKey(
        Providers,
        related_name='user_phone',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Locations(models.Model):
    lan = models.FloatField()
    len = models.FloatField()
    user = models.ForeignKey(
        User,
        related_name='user_location',
        on_delete=models.CASCADE
    )
    whereHouses = models.ForeignKey(
        WhereHouses,
        related_name='where_houses_location',
        on_delete=models.CASCADE
    )
    povider = models.ForeignKey(
        Providers,
        related_name='povider_location',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Cities(models.Model):
    city = models.CharField(max_length=50)
    location = models.ForeignKey(
        Locations,
        related_name='locations_city',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Areas(models.Model):
    area = models.CharField(max_length=50)
    location = models.ForeignKey(
        Locations,
        related_name='locations_area',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

