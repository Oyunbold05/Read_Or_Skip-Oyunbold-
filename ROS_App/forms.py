# forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)  # Radio buttons for rating

    class Meta:
        model = Review
        fields = ['review', 'summary', 'rating']
