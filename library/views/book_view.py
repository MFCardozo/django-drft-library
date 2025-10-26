from rest_framework import viewsets
from library.models.book import Book
from library.serializers.book_serializer import BookSerializer
from rest_framework.decorators import action
from django.db.models import Count, Avg, Max, Min
from rest_framework.response import Response
from django.db.models import IntegerField


class BookViewSet(viewsets.ModelViewSet):
    # preload authors
    queryset = Book.objects.prefetch_related("authors").all()
    serializer_class = BookSerializer

    # /books/stats
    @action(detail=False, methods=["get"])
    def stats(self, request):
        """
        Return aggregated statistics about books.
        """
        queryset = self.get_queryset().annotate(authors_count=Count("authors"))
        data = queryset.aggregate(
            total_books=Count("id"),
            avg_authors_per_book=Avg("authors_count", output_field= IntegerField()),
            max_authors_per_book = Max("authors_count"),
            avg_pages=Avg("pages", output_field=IntegerField()),
            max_pages=Max("pages"),
            min_pages=Min("pages"),
        )
        return Response(data)