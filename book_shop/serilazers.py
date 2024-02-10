from .models import Category, Book, Author
from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name')
    author_status = serializers.BooleanField(source='author.status')
    class Meta:
        model = Book
        fields = ('author_name', 'description', 'audio', 'category', 'name', 'isbn', 'photo', 'file', 'author_status', 'download_count')

class CategorySerialazer(serializers.ModelSerializer):
    book_category = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name', 'book_category')

class AuthorSerializer(serializers.ModelSerializer):
    book_author = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('full_name', 'book_author')

