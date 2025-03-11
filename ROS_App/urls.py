from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
<<<<<<< HEAD
    path('login/', views.login_view, name='login'), 
=======
    path('', views.login_view, name='login'), 
>>>>>>> 09cd31530b41322c48d3c0fc6d95748b0b98dc46
    path('home/', views.home_view, name='home'), 
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]