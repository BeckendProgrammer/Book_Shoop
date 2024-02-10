from django.contrib import admin
from .models import Category, Author, Book
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_at')
    list_filter= ('created_at', 'status',)
    search_fields = ('name', )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',  'created_at')
    list_filter= ( 'created_at', )
    search_fields = ('full_name', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'category', 'author', 'isbn')
    list_filter= ('status', 'created_at', 'category', 'author')
    search_fields = ('name', 'description', 'category', 'author', 'isbn')