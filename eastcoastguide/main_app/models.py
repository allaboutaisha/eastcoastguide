from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


NUMS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

PRICE = (
    ('$', '$'),
    ('$$', '$$'),
    ('$$$', '$$$'),
    ('$$$$', '$$$$'),
)
     
LOCATIONS = (
    ('NY', 'NY'),
    ('MA', 'MA'),
)

# Create your models here
    
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(
        max_length=2,
        choices=LOCATIONS,
        default=LOCATIONS[0][0])
    website = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    price_range = models.CharField(
        max_length=5,
        choices=PRICE,
        default=PRICE[0][0])
    type = models.CharField(
        'Cuisine',
        max_length=100)
    hours = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    comment = models.TextField(max_length=250)
    rating = models.CharField(
        max_length=1,
        choices=NUMS,
        default=NUMS[0][0]
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


    