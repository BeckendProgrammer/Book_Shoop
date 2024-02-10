from django.shortcuts import render
from .models import Author, Category, Book
from book_shop.serilazers import CategorySerialazer, BookSerializer, AuthorSerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySerialazer
    permission_classes = [AllowAny]


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.filter(status=True)
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.filter(status=True)
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
