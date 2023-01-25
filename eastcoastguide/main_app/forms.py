from django.forms import ModelForm
from .models import Comment, Restaurant

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['user', 'date', 'comment', 'rating']

class ResturantForm(ModelForm):
  class Meta:
    model = Restaurant
    fields = ['name', 'location', 'website', 'address', 'price_range', 'type', 'hours', 'image']


