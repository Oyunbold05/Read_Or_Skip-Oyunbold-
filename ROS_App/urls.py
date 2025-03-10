from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.login_view, name='login'), 
    path('home/', views.home_view, name='home'), 
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]