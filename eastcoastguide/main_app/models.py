from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)

class Restaurant(models.Model):
    location = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    price_range = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    hours = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    comment = models.ManyToManyField(Comment) # We might not need this
    user = models.ForeignKey(User, on_delete=models.CASCADE)