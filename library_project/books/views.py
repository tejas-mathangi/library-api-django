from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books' # Default is 'object_list'
    paginate_by = 10 # Number of books per page
