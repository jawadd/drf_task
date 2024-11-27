from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from decimal import Decimal
from myapp.models import Book, Log


@receiver(pre_save, sender=Book)
def validate_and_set_default_price(sender, instance, **kwargs):
    if isinstance(instance.price, str):
        instance.price = Decimal(instance.price)
    if instance.price is None:
        instance.price = Decimal('10.00')
    if instance.price < Decimal('0.0'):
        raise ValidationError("Price cannot be negative.")

@receiver(post_save, sender=Book)
def create_log_entry(sender, instance, created, **kwargs):
    if created:
        message = f"New book '{instance.title}' added."
    else:
        message = f"Book '{instance.title}' updated."

    # Log the message after the book is saved
    Log.objects.create(book=instance, message=message)
