

from django.urls import path
from . import views

urlpatterns = [    
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('restaurant/<str:location>/', views.RestaurantsIndex.as_view(), name='restaurants'),
    path('restaurant/<str:location>/<int:pk>/', views.RestaurantDetail.as_view(), name='detail'),
    path('create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurant/<str:location>/<int:pk>/add_comment', views.CommentCreate.as_view(), name='comment_create'),
    path('restaurant/<str:location>/<int:pk>/update', views.RestaurantUpdate.as_view(), name='restaurant_update'),
    path('restaurant/<str:location>/<int:pk>/delete', views.RestaurantDelete.as_view(), name='restaurant_delete')                                      
]