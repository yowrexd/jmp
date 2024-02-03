from django.contrib import admin
from .models import Reservation, Room, ContactUs, CustomerInfo, Hotel, Admin, Review

admin.site.register(Admin)
admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(ContactUs)
admin.site.register(CustomerInfo)
admin.site.register(Review)