import uuid
from django.db import models
from UserApp.models import User


# Create your models here.


class Product(models.Model):
    class Currency(models.TextChoices):
        YEMEN = 'E'
        SAUDI_ARABIA = 'S'
    name = models.CharField(max_length=20)
    price = models.FloatField()
    state = models.CharField(max_length=50)
    desc_ar = models.TextField()  # change for bellow relation
    # desc = models.ForeignKey(
    #     Description,
    #     related_name='product_description',
    #     on_delete=models.CASCADE
    # )
    owner = models.ManyToManyField(User)
    puyer = models.ManyToManyField(User, related_name='Puyer')
    seller = models.ManyToManyField(User, related_name='Seller')
    currency = models.TextField(
        choices=Currency.choices,
        default=Currency.YEMEN
    )
    serial_number = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Depatments(models.Model):
    title = models.CharField(max_length=50)
    subDep = models.ForeignKey(
        'self',
        related_name='sub_dep',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='product_departments',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class WhereHouses(models.Model):
    title = models.CharField(max_length=50)
    User = models.ForeignKey(
        User,
        related_name='user_where_house',
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        Product,
        # through='ProductWhereHouseRelstions'
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Providers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # proof = models.CharField(max_length=50) //determodels.Model the type
    provide = models.ManyToManyField(Product, related_name='providers_product')
    store = models.ManyToManyField(
        WhereHouses, related_name='store_product_from_providers')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Bills(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_bill',
        on_delete=models.CASCADE
    )
    providers = models.ForeignKey(
        Providers,
        related_name='user_where_house',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Oprations(models.Model):
    class Types(models.TextChoices):
        SELLER = 'S'
        BUYER = 'B'

    user = models.ForeignKey(
        User,
        related_name='user_oprations',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='user_oprations',
        on_delete=models.CASCADE
    )
    bills = models.ForeignKey(
        Bills,
        related_name='user_oprations',
        on_delete=models.CASCADE
    )
    typeChoice = models.TextField(choices=Types.choices)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "product", "bills"), )


class ProductType(models.Model):
    class ChoiseType(models.TextChoices):
        SIGLER = 'S'
        PLORUL = 'P'
    type = models.CharField(choices=ChoiseType.choices, max_length=10)
    count = models.FloatField()
    product = models.ForeignKey(
        Product,
        related_name='product_type',
        on_delete=models.CASCADE
    )
    bill = models.ForeignKey(
        Bills,
        related_name='bill_type',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ProductWhereHouseRelstions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    whereHouses = models.ForeignKey(WhereHouses, on_delete=models.CASCADE)
    state = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
