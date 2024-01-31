from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
# from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm
from .models import Author, Book, Review


class IndexView(ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.order_by('-create_at')


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()  # Get the book object
        book_reviews = Review.objects.filter(book=book)  # Filter reviews related to this book
        context['book_reviews'] = book_reviews  # Add book reviews to context
        return context


class ReviewCreateView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            body = request.POST.get('review', '')
            book_id = kwargs.get('pk')
            new_review = Review(body=body, book_id=book_id, user=request.user)
            new_review.save()
        return redirect('home')  # Kerakli sahifaga qaytish

    # Kerak emas, lekin agar GET so'rovi kelgan bo'lsa, 405 Method Not Allowed xatolikni qaytarish uchun
    def get(self, request, *args, **kwargs):
        return redirect('home')


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context_dict = {
        'books': books,
    }
    return render(request, 'books/author_books.html', context_dict)
