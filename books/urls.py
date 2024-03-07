from django.urls import path
from django.contrib import admin

from books.views import IndexView, BookDetailView, ReviewCreateView, author


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/review/', ReviewCreateView.as_view(), name='review'),
    path('<str:author>/', author, name='author_books'),
]
