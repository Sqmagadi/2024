from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=8, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=1)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2, null=True, blank=True)
    percentage_discount = models.DecimalField(default=0, max_digits=5, decimal_places=0, null=True, blank=True)
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_sale and self.sale_price < self.price:
            self.discount = round(self.price - self.sale_price, 2)
            self.percentage_discount = round((self.discount / self.price) * 100)
        else:
            self.discount = 0
            self.percentage_discount = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profiles/customers/')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product
    
    