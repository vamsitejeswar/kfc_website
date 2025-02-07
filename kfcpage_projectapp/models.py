from django.db import models

# Create your models here.
class items(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class INTERNATIONAL_BURGER_FEST(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class MATCH_DAY_COMBOS(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class VALUE_LUNCH_SPECIALS(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class BOX_MEAL(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class BURGERS(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class CHICKEN_BUCKETS(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_actualprice=models.DecimalField(max_digits=10, decimal_places=2)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class RICE_BOWLZ(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)

class SNACKS(models.Model):
    order_name=models.CharField(max_length=100)
    order_item=models.CharField(max_length=100)
    order_quantity=models.CharField(max_length=100)
    order_price=models.DecimalField(max_digits=10, decimal_places=2)
    order_details=models.CharField(max_length=100)