from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .forms import ReviewForm
from .models import Author, Book, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'
    login_url = 'user:login'
    model = Book
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = self.get_queryset()
        page_num = self.request.GET.get('page', 1)
        paginator = Paginator(books, self.paginate_by)

        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context['page_obj'] = page_obj
        return context

# def book_list(request):
#     book = Book.objects.all().order_by('-create_at')
#     paginator = Paginator(book, 3)
#     page_number = request.GET.get('page', 1)
#     books = paginator.page(page_number)
#     context = {'books': books}
#     return render(request,'books/index.html', context=context)


def download_book(pk):
    book = get_object_or_404(Book, pk=pk)
    if hasattr(book, 'pdf'):
        response = HttpResponse(book.pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(book.title)
        return response
    else:
        return HttpResponse("PDF file not found.")


class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = 'books/detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        pdf_url = None
        if hasattr(book, 'pdf'):
            pdf_url = book.pdf.url
        context['pdf_url'] = pdf_url
        context['authors'] = book.authors.all()
        context['book_reviews'] = Review.objects.filter(book=book)

        return context


class ReviewCreateView(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            book_id = kwargs.get('pk')
            body = request.POST.get('review', '')
            new_review = Review(body=body, book_id=book_id, user=request.user)
            new_review.save()
            return redirect('detail', pk=book_id)
        return redirect('home')


@login_required(login_url='login')
def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context_dict = {
        'books': books,
    }
    return render(request, 'books/author_books.html', context_dict)

# @login_required(login_url='login')
# def add_comment(request):
#     if request.method == 'POST':
#         form = AddCommentForm(request.POST)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return redirect('author_books')
#     else:
#         form = AddCommentForm()
#     return render(request, 'add_comment.html', {'form': form})
