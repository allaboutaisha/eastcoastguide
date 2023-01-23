from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    rating = models.CharField(
        max_length=1,
        choices=NUMS,
        default=NUMS[0][0]
    )class User(models.Model):
    _id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)

class Restaurant(models.Model):
    location = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    comment = models.ManyToManyField(Comment) # We might not need this
    user = models.ForeignKey(User, on_delete=models.CASCADE)