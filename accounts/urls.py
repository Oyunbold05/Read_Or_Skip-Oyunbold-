from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.user_login, name="login")
]