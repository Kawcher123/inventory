from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Customer(models.Model):
	STATUS = (
			('Active', 'Active'),
			('Inactive', 'Inactive'),
			)

	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address=models.CharField(max_length=200, null=True,default="")
	status = models.CharField(max_length=200, null=True, choices=STATUS, default="Active")
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 
	STATUS = (
			('In Stock', 'In Stock'),
			('Out of Stock', 'Out of Stock'),
			)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default="In Stock")
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)


	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
	product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.customer)