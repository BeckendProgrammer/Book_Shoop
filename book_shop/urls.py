from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewset,AuthorViewset,BookViewset


router = routers.DefaultRouter()

router.register('Category',CategoryViewset, basename='category')
router.register('Author',AuthorViewset, basename='author')
router.register('Book',BookViewset, basename='book')


urlpatterns=[
    path('', include(router.urls))
]
