from django.urls import path
from .views import register, LoginAPI, post_list, post_detail

urlpatterns = [
    path('api/register/', register, name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/posts/', post_list, name='post-list'),
    path('api/posts/<int:pk>/', post_detail, name='post-detail'),
]
