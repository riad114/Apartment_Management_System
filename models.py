from django.db import models

# Create your models here.
class User(models.Model):
   
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    user_type = models.CharField(max_length=10)


class Apartments(models.Model):
    # user_id = models.ForeignKey('User',null=True,on_delete=models.SET_NULL)
    flat_number = models.CharField(max_length=30)
    building_name = models.CharField(max_length=30)
    building_number = models.CharField(max_length=30)
    building_address = models.CharField(max_length=30)
    flat_size = models.CharField(max_length=30)
    num_of_beds = models.CharField(max_length=30)
    num_of_toilet = models.CharField(max_length=30)
    num_of_balcony = models.CharField(max_length=30)
    map_address = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    class Meta:
        db_table='ourproject_apartments'
    

class bill(models.Model):
    user_id = models.ForeignKey('User',null=True,on_delete=models.SET_NULL)
    type_of_bill = models.CharField(max_length=30)
    bill_number = models.CharField(max_length=50)
    paid_amount = models.CharField(max_length=30)
    bill_month = models.CharField(max_length=20)

class complaint_section(models.Model):
    user_id = models.ForeignKey('User',null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    home_address = models.CharField(max_length=500)
    police_station = models.CharField(max_length=50)

