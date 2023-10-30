from django.shortcuts import render, get_object_or_404

from .models import Book
from .utils import average_rating, get_book_details


def index(request):
    return render(request, 'reviews/base.html')


def search_result(request):
    search_text = request.GET.get('search', '')
    return render(request,
                  'reviews/search_result.html',
                  {'search_text': search_text})


def book_list(request):
    books = Book.objects.all()
    context = {
        'book_list': [get_book_details(book) for book in books]
    }
    return render(request, 'reviews/book_list.html', context)


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    context = {
        'book_details': get_book_details(book),
        'reviews': reviews
    }
    return render(request, 'reviews/book_details.html', context)
