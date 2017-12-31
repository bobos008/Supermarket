from django.db import models

# Create your models here.
class Seller(models.Model):
    s_name = models.CharField(max_length=32)
    s_password = models.CharField(max_length=64)

class Buyer(models.Model):
    b_name = models.CharField(max_length=32)
    b_password = models.CharField(max_length=64)
