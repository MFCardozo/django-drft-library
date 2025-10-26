from __future__ import annotations

from django.db.models import Count, Avg
from rest_framework import viewsets
from library.models.author import Author
from library.serializers.author_serializer import AuthorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        #  add book_count annotation for top_authors
        return qs.annotate(book_count=Count("books"))
    
    # /authors/top_authors
    @action(detail=False, methods=["get"])
    def top_authors(self, request):
        """Return authors ordered by number of books (descending)."""
        qs = self.get_queryset().order_by("-book_count")[:10]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
