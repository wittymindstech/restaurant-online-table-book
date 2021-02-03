from django.contrib import admin
from .models import BookTable,Order,Restaurant
# Register your models here.
admin.site.register(BookTable)
admin.site.register(Order)
admin.site.register(Restaurant)