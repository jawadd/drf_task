from rest_framework import serializers
from decimal import Decimal
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date', 'price', 'created_at']

    def validate_price(self, value):
        # Ensure the price is a valid Decimal and non-negative
        if value < Decimal('0.0'):
            raise serializers.ValidationError("Price cannot be negative.")
        return value
    
    def validate_isbn(self, value):
        if not self.instance:  # This will be True only when creating a new book
            if Book.objects.filter(isbn=value).exists():
                raise serializers.ValidationError("A book with this ISBN already exists.")
        return value
