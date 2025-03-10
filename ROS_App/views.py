from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Book, TBR, Review
from .forms import ReviewForm

# View to handle the book detail page
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        new_review = form.save(commit=False)
        new_review.user = request.user
        new_review.book = book
        new_review.save()
        return redirect('book_detail', book_id=book.id)
    
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

# View to handle adding books to TBR (To Be Read) list
def add_to_tbr(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user.is_authenticated:
        TBR.objects.create(user=request.user, book=book)
        messages.success(request, "Book added to your To Be Read list!")
    return redirect('book_detail', book_id=book.id)
