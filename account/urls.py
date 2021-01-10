from django.urls import path
from . import views 
from .views import AddCustomer,UpdateCustomer,AddProduct,UpdateProduct

urlpatterns = [
    path('',views.home,name="home"),
    path('add_product/',AddProduct.as_view(),name="add_product"),
    path('edit_product/edit/<str:pk>',UpdateProduct.as_view(),name="edit_product"),
    path('product',views.product,name="product"),
    path('add_customer/',AddCustomer.as_view(),name="add_customer"),
    path('edit_customer/edit/<str:pk>',UpdateCustomer.as_view(),name="edit_customer"),
    path('customer_list/',views.customerList,name="customer_list"),
    path('customer/<str:pk>/',views.customer,name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('sales_report/', views.salesReport, name="sales_report"),
]