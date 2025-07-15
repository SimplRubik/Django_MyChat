from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, views_auth

app_name = 'chat'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<str:room_name>/', views.room_detail, name='room_detail'),
    path('register/', views_auth.RegisterView.as_view(), name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
