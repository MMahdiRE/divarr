from django.db import models
from users.models import CustomUser

class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('sold', 'Sold')])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="ads")

    def __str__(self):
        return self.title
