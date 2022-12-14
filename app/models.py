from django.db import models
import uuid


class Owner(models.Model):
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=30, blank=False)
    phone = models.PositiveIntegerField(max_length=12, blank=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=False)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    username = models.CharField(blank=False, max_length=28)
    password = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False)
    rate = models.IntegerField(blank=False)
    qty = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
