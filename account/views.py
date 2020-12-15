from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Customer,Order
from .forms import OrderForm
# Create your views here.


def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'dashboard.html', context)


def salesReport(request):
	return render(request,'sales_report.html',{})



def product(request):
	products = Product.objects.all()
	total_product=products.count()

	return render(request, 'product.html', {'products':products,'total_product':total_product})

def customerList(request):
	customers = Customer.objects.all()
	return render(request,'customer_list.html',{'customer_list':customers})


def customer(request,pk):
	customers = Customer.objects.get(id=pk)

	orders = customers.order_set.all()
	order_count = orders.count()

	context = {'customer':customers, 'orders':orders, 'order_count':order_count}
	return render(request, 'customer.html',context)



def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)



def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'delete.html', context)


