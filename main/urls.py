# main/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer/add/', views.customer_add, name='customer_add'),
    path('customer/<int:customer_id>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
    
    path('services/', views.service_list, name='service_list'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('service/add/', views.service_add, name='service_add'),
    path('service/<int:service_id>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:service_id>/delete/', views.service_delete, name='service_delete'),

    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscription/<int:subscription_id>/', views.subscription_detail, name='subscription_detail'),
    path('subscription/add/', views.subscription_add, name='subscription_add'),
    path('subscription/<int:subscription_id>/edit/', views.subscription_edit, name='subscription_edit'),
    path('subscription/<int:subscription_id>/delete/', views.subscription_delete, name='subscription_delete'),
    
    path('subscription/<int:subscription_id>/', views.subscription_detail, name='subscription_detail'),
    #path('subscription/<int:subscription_id>/pdf/', views.subscription_detail_pdf, name='subscription_detail_pdf'),
    path('signup/', views.signup, name='signup'),
]


