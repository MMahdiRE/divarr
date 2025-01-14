
from django.db import models
from ads.models import Ad

class Payment(models.Model):
    ad = models.OneToOneField(Ad, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
