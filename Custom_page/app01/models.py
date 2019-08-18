from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)