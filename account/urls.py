from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('product',views.product,name="product"),
    path('customer_list/',views.customerList,name="customer_list"),
    path('customer/<str:pk>/',views.customer,name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('sales_report/', views.salesReport, name="sales_report"),
]