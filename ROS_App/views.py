from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home_view(request):
    # Example data (replace with database queries later)
    trending_books = [
        {'title': 'Dracula', 'author': 'Bram Stoker', 'cover': 'dracula.jpg'},
        {'title': 'The Little Prince', 'author': 'Antoine de Saint-Exupéry', 'cover': 'thelittleprince.jpg'},
        {'title': 'Lord of the Rings', 'author': 'J.R.R. Tolkien', 'cover': 'lordoftherings.jpg'},
    ]
    categories = ['Fantasy', 'Classics', 'Thriller', 'Romance']

    context = {
        'trending_books': trending_books,
        'categories': categories,
    }
    return render(request, 'ROS_App/home.html', context)

def login_view(request):
    return render(request, 'ROS_App/login.html')

def logout_view(request):
    return render (request, 'ROS_App/logout.html')

def register_view(request):
    return render(request, 'ROS_App/register.html')

def user_register(request):
    return render(request, 'ROS_App/register.html')

def user_login(request):
    return render(request, "ROS_App/login.html")

def user_logout(request):
    return render(request, "ROS_App/logout.html")