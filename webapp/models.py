from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    room_type = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    facilities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.room_type} - {self.capacity} people"

class Reservation(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField(null=True)
    comments = models.TextField(blank=True)

    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Contact Us: {self.subject} - {self.name}"
    
class CustomerInfo(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.name} for {self.hotel.name} - {self.rating} stars"

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)