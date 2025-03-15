from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('login/', views.login_view, name='login'), 
    path('home/', views.home_view, name='home'), 
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('aboutUs/',views.aboutUs_view, name='aboutUs'),
    path('faq/', views.faq_view, name='faq'),
    path('contactUs/', views.contactUs_view, name='contactUs'),
    path('myAccount/',views.myAccount_view, name="myAccount"),
]