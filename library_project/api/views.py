from rest_framework import generics
from .serializers import BookSerializer
from books.models import Book

class BookAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all() # Placeholder for queryset
    # def get_queryset(self):
    #     from books.models import Book
    #     return Book.objects.all() 