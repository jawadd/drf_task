from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal

from .models import Book, Log

class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Django for Beginners",
            "author": "William Vincent",
            "isbn": "1234567890123",
            "published_date": "2023-01-01",
            "price": Decimal('15.00')
        }

    def test_create_book_success(self):
        """Test creating a book with valid data."""
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().title, "Django for Beginners")

    def test_retrieve_book(self):
        """Test retrieving a specific book by its ID."""
        book = Book.objects.create(**self.book_data)
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_create_book_with_negative_price(self):
        """Test creating a book with a negative price should fail."""
        self.book_data['price'] = "-5.00"
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

    def test_update_book_and_check_log(self):
        """Test updating a book and verify that a log entry is created."""
        book = Book.objects.create(**self.book_data)
        update_data = { "title": "Django",
        "author": "jawad+",
        "isbn": "9844",
        "published_date": "2024-11-27",
        "price": "44.44",
        "created_at": "2024-11-27"}

        response = self.client.put(f'/api/books/{book.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify log creation
        log_entry = Log.objects.filter(book=book).last()
        self.assertIsNotNone(log_entry)
        self.assertIn("updated", log_entry.message)

