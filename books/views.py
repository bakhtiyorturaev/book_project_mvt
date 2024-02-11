from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .forms import ReviewForm
from .models import Author, Book, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class IndexView(ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'
    login_url = 'login/'

    def get_queryset(self):
        return Book.objects.order_by('-create_at')


class BookDetailView(LoginRequiredMixin,DetailView):
    template_name = 'books/detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


class ReviewCreateView(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            body = request.POST.get('review', '')
            book_id = kwargs.get('pk')
            new_review = Review(body=body, book_id=book_id, user=request.user)
            new_review.save()
        return redirect('home')

    def get(self, request, *args, **kwargs):
        return redirect('home')


@login_required(login_url='login')
def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context_dict = {
        'books': books,
    }
    return render(request, 'books/author_books.html', context_dict)
