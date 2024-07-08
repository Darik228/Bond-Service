from django.db import models
from django.contrib.auth.models import User


class Bond(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    isin = models.CharField(max_length=12, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    purchase_date = models.DateField()
    maturity_date = models.DateField()
    interest_payment_frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.isin})"



