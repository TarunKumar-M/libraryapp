from django.views.generic import ListView
from django.shortcuts import render

from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template = "book_list.html"