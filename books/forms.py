from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'book', 'user', 'body'
        )

