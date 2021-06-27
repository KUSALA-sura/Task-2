from django.db import models

# Create your models here.

class profile(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=30)
	age=models.IntegerField()
	rollno=models.CharField(max_length=10)
	addres=models.TextField(null=True)
	percentage=models.DecimalField(max_digits=6, decimal_places=4)
	dob=models.DateField()
	timet=models.DateTimeField(auto_now=True)
	img =models.ImageField(upload_to = "images/")
	price=models.FloatField(null=True)
	upload = models.FileField(upload_to ="uploads/")