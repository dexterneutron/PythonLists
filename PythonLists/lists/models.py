from django.db import models

class Tasks(models.Model):
    description = models.TextField()

class ShoppingItem(models.Model):
    Name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.CharField(max_length=30)
