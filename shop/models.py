from django.db import models

from users.models import Student


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)


class Shop_history(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shop_history_product')
    buyer = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='shop_history_buyer')
    purchase_date = models.DateTimeField(auto_now_add=True)

