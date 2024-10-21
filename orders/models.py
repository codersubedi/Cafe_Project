from django.db import models
from menu.models import MenuItem
from customers.models import Customer

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
