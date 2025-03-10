from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Book details and reviews
    path('book/<int:book_id>/add_to_tbr/', views.add_to_tbr, name='add_to_tbr'),  # Add to TBR
]
