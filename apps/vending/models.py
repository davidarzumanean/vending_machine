from django.db import models
from decimal import Decimal
from uuid import uuid4
from django.core.validators import MinValueValidator


class Product(models.Model):
    class Meta:
        db_table = "product"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.DecimalField(max_digits=5, decimal_places=0, validators=[MinValueValidator(Decimal("0"))])
    logo = models.URLField(max_length=200)
    color = models.CharField(max_length=7, default="#ffffff")


class User(models.Model):
    class Meta:
        db_table = "user"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_name = models.CharField(max_length=25)
    balance = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
