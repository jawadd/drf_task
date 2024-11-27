from django.db import models
from django.core.validators import  MinValueValidator

    
class Book(models.Model):
    title= models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn=  models.CharField(unique=True, max_length=50)
    published_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,validators = [MinValueValidator(0.0)], default=10)
    created_at = models.DateField(auto_now_add=True)
    time_stamp= models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Log(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log for {self.book.title} - {self.message}'