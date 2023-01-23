from django.urls import path
from . import views

urlpatterns = [    
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('restaurants/', views.RestaurantsNYIndex.as_view(), name='index'),
    path('restaurants/<int:restaurant_id>/', views.RestaurantDetail.as_view(), name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create')
]