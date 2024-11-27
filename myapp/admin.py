from django.contrib import admin
from .models import Book, Log

# Register your models here.
admin.site.register(Book)
admin.site.register(Log)