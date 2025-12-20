from django.urls import path
from account import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.HomeView.as_view(), name='home'),  # додайте домашню сторінку
    path('register/', views.RegisterView.as_view(), name='register')
]
