from django.db import models
from store_app.models import Color
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model

user = get_user_model()

TRANSACTION_CHOICES = (
    (False , 'failed'),
    (True , 'success'),
)

class Order(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    transaction = models.OneToOneField('Transaction', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)  # اضافه کردن رنگ
    count = models.PositiveIntegerField()

    def __str__(self):
        if self.color:
            return f"{self.count} of {self.product.name} ({self.color.color_name})"
        return f"{self.count} of {self.product.name} (No Color)"

class Basket(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return f"Basket of {self.user}"

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        if self.color:
            return f"{self.count} of {self.product.name} ({self.color.color_name})"
        return f"{self.count} of {self.product.name} (No Color)"

class Transaction(models.Model):
    status = models.BooleanField(default=False, choices=TRANSACTION_CHOICES)
    ref_code = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f"Transaction {self.ref_code} - {self.status}"
