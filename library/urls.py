from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views.author_view import AuthorViewSet
from library.views.book_view import BookViewSet

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename= "author")
router.register("books", BookViewSet, basename="book")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]