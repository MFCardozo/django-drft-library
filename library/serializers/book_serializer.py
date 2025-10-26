from rest_framework import serializers
from library.models.book import Book
from library.serializers.author_serializer import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'