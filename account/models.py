from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


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


	def get_absolute_url(self):
		return reverse("customer", kwargs={"pk": self.pk})
	


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

	def get_absolute_url(self):
		return reverse("home")
	

	def __str__(self):
		return self.name + str(self.price)

class ProductOrder(models.Model):
	vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,blank=True)
	product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	quantity=models.IntegerField(default=0,null=True,blank=True)
	date_ordered=models.DateField(auto_now_add=True)
	complete=models.BooleanField(default=False,null=True,blank=False)
	transaction_id=models.CharField(max_length=300,null=True)

	def __str__(self):
	    return str(self.id)

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
	product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	order=models.ForeignKey(ProductOrder,on_delete=models.SET_NULL,null=True)
	quantity=models.IntegerField(default=0,null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.product)