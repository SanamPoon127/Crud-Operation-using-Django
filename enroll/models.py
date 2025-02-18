from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=127)
    email = models.EmailField(max_length=127)
    password = models.CharField(max_length=100)