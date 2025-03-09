from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'ROS_App/login.html')

def register_view(request):
    return render(request, 'ROS_App/register.html')

def user_register(request):
    return render(request, 'ROS_App/register.html')

def user_login(request):
    return render(request, "ROS_App/login.html")