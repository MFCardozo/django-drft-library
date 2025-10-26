from __future__ import annotations
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models.author import Author
from .models.book import Book


class LibraryAPITestCase(APITestCase):
    def setUp(self)-> None:
        self.author = Author.objects.create(first_name="Test", last_name="Author")

        self.book = Book.objects.create(title="Test Book", isbn="1234567890123", pages=100, publication_date="1999-01-01")
        self.book.authors.add(self.author)

    def test_list_books(self):
        url = reverse("book-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)        

    def test_create_author(self):
        url = reverse("author-list")
        payload = {"first_name": "New", "last_name": "Writer"}
        resp = self.client.post(url, payload, format="json")
    
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Author.objects.filter(first_name="New",
            last_name="Writer").exists())
    
    def test_create_book(self):
        url = reverse("book-list")
        payload = {"title": "Test", "publication_date": "2000-01-01", "isbn" : "1234", "pages": 200, "authors" : [1]}
        resp = self.client.post(url, payload, format="json")
    
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="Test",
            isbn="1234").exists())
        
    def test_book_stats(self):
        url = reverse("book-stats")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        expected_data = {
            "total_books": 1,
            "avg_authors_per_book": 1,
            "max_authors_per_book": 1,
            "avg_pages": 100,
            "max_pages": 100,
            "min_pages": 100,
        }

        for key, value in expected_data.items():
            self.assertEqual(resp.data[key], value, f"Error in field '{key}'")
