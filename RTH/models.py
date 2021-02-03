from django.db import models
from django_mysql.models import ListCharField
import jsonfield
# Create your models here.
class BookTable(models.Model):
    name=models.CharField(max_length=200,null=True)
    booking_date_time=models.DateTimeField(auto_now_add=True)
    table_book_time=models.TimeField(null=True)
    table_book_date=models.CharField(max_length=50,null=True)
    num_of_person=models.IntegerField(null=True)
    contact_num=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.IntegerField()
    table_id=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    booking_name=models.CharField(max_length=100)
    total_amount=models.CharField(max_length=100)
    each_contribution=jsonfield.JSONField()
    #list_of_people=ListCharField(base_field=models.CharField(max_length=10),size=6,max_length=(6 * 11))
    def __str__(self):
        return self.booking_name
class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=10)
    address=models.TextField()
    def __str__(self):
        return self.name


