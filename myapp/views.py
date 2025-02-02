from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
