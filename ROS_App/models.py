from django.db import models
from django.contrib.auth.models import User

# Model for Books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='books/covers/', default='images/dracula.jpg')
    
    def __str__(self):
        return self.title

# Model for TBR (To Be Read)
class TBR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

# Model for Reviews
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    summary = models.TextField(null=True, blank=True)  # Optional summary field
    rating = models.IntegerField()  # A simple rating from 1-5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.book.title}"
