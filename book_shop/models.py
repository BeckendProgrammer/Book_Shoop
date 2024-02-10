from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Nomi')
    status = models.BooleanField(default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
    




class Author(models.Model):
    full_name = models.CharField(max_length=30, verbose_name = 'F.I.SH')

    status = models.BooleanField(default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Mualif'
        verbose_name_plural = 'Mualiflar'
        ordering = ('-created_at', )

    def __str__(self):
        return self.full_name
    




class Book(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank=True, null=True, verbose_name = 'Kategoriyasi', related_name='book_category')
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, blank = True, null = True, verbose_name = 'Mualifi', related_name='book_author') 
    name = models.CharField(max_length = 30, verbose_name = 'Kitob nomi')
    status = models.BooleanField(default = True, verbose_name = 'Holati')
    description = models.TextField(verbose_name='Ta\'rif')
    photo = models.ImageField(upload_to='books_photo/%Y/%m/%d/', blank=True, null=True, verbose_name='Rasm')
    isbn = models.PositiveIntegerField(unique=True, verbose_name='ISBN')
    file = models.FileField(upload_to='book_file/%Y/%m/%d', verbose_name='Kitobninng PDF Shakli', blank=True, null=True)
    audio = models.FileField(upload_to='book_file/%Y/%m/%d', verbose_name='Kitobning Audio Shakli', blank=True, null=True)
    download_count = models.PositiveIntegerField(default=0, verbose_name='Yuklab Olishlar Soni')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name= 'Kitob'
        verbose_name_plural = 'Kitoblar'
        ordering = ('-created_at', 'author')


    def __str__(self):
        return self.name









    