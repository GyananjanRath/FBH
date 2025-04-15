from django.db import models

# Create your models here.
class Account(models.Model):
    name =  models.CharField(max_length=32)
    DOB  = models.DateField()
    Aadhar = models.BigIntegerField()
    pan =  models.CharField(max_length = 10)
    mobile = models.IntegerField()
    address =  models.TextField(max_length = 40)
    acc = models.BigAutoField(primary_key = True)
    bal = models.DecimalField(decimal_places= 2 , max_digits = 9 , default = 1000.0)  
    pin = models.IntegerField(default = 0)
    email = models.EmailField(default = "gyananjanrath123@gmail.com")
    otp = models.IntegerField(default = 0)