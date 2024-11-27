from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from myapp.models import Book, Log


@receiver(pre_save, sender=Book)
def validate_and_set_default_price(sender, instance, **kwargs):
   
    if instance.price is None:
        instance.price = 10.00

    if instance.price < 0:
        raise ValidationError("Price cannot be negative.")

@receiver(post_save, sender=Book)
def log_book_creation(sender, instance, created, **kwargs):
    if created:
        message = f"A new book '{instance.title}' has been added."
    else:
        message = f"The book '{instance.title}' has been updated."
    
    Log.objects.create(book=instance, message=message)
