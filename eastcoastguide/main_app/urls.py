from django.urls import path
from . import views

urlpatterns = [    
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('restaurants/<str:location>/', views.RestaurantsIndex.as_view(), name='restaurants'),
    path('restaurants/<int:restaurant_id>/', views.RestaurantDetail.as_view(), name='detail'),
    path('create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
    path('comments/create/', views.CommentCreate.as_view(), name='comments_create')                                      
]