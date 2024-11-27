from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date','price', 'created_at']