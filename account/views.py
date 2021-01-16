from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Customer,Order,ProductOrder
from .forms import OrderForm
from django.http import JsonResponse
from django.views.generic import CreateView,UpdateView
from .forms import CustomerForm,ProductForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
# Create your views here.






def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'form': forms}
    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')




@login_required(login_url='/login/')
def home(request):
	orders = Order.objects.all()
	products = Product.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	total_products = products.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,'total_products':total_products,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'dashboard.html', context)

@login_required(login_url='/login/')
def salesReport(request):
	return render(request,'sales_report.html',{})

@method_decorator(login_required, name='dispatch')
class AddProduct(CreateView):
	model=Product
	template_name="addproduct.html"
	form_class=ProductForm

@method_decorator(login_required, name='dispatch')
class UpdateProduct(UpdateView):
	model=Product
	template_name="update_product.html"
	form_class=ProductForm

@login_required(login_url='/login/')
def product(request):
	products = Product.objects.all()
	total_product=products.count()
	instock=products.filter(status='In Stock').count()

	return render(request, 'product.html', {'products':products,'total_product':total_product,'instock':instock})

@method_decorator(login_required, name='dispatch')
class AddCustomer(CreateView):
	model=Customer
	template_name="addcustomer.html"
	form_class=CustomerForm

@method_decorator(login_required, name='dispatch')
class UpdateCustomer(UpdateView):
	model=Customer
	template_name="update_customer.html"
	form_class=CustomerForm

@login_required(login_url='/login/')
def customerList(request):
	customers = Customer.objects.all()
	total_customers = customers.count()
	active = customers.filter(status='Active').count()
	inactive = customers.filter(status='Inactive').count()
	return render(request,'customer_list.html',{'customer_list':customers,'total_customers':total_customers,'active':active,'inactive':inactive})


@login_required(login_url='/login/')
def customer(request,pk):
	customers = Customer.objects.get(id=pk)

	orders = customers.order_set.all()
	order_count = orders.count()

	context = {'customer':customers, 'orders':orders, 'order_count':order_count}
	return render(request, 'customer.html',context)



@login_required(login_url='/login/')
def createOrder(request):
	orders=ProductOrder.objects.all()
	products=Product.objects.all()
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		if request.user.is_authenticated:
			vendor=request.user.vendor
			id=request.POST.get('sid')
			productname=Product.objects.get(pk=id)
			print(productname)
			productorder,created=ProductOrder.objects.get_or_create(vendor=vendor,product=productname,complete=False)
			orderItem,created=Order.objects.get_or_create(order=productorder,product=productname)
			items=productorder.order_set.all()
			#print(items)
			odata=ProductOrder.objects.values()
			norder=list(odata)
			print(odata)
			form = OrderForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')
			return JsonResponse({'status':'save','order_data':norder})
		else:
			return JsonResponse({'status':0})

	context = {'form':form,'orders':orders,'products':products}
	return render(request, 'order_form.html', context)



@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'delete.html', context)


