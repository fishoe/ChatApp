from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)