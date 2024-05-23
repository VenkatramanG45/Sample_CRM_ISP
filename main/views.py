from django.shortcuts import render

# Create your views here.
# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Service

from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Service, Subscription
from .forms import CustomerForm, ServiceForm, SubscriptionForm

from django.contrib.auth.decorators import login_required

import pdfkit
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Subscription
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    customers = Customer.objects.all()
    services = Service.objects.all()
    subscriptions = Subscription.objects.all()
    context = {
        'customers': customers,
        'services': services,
        'subscriptions': subscriptions
    }
    return render(request, 'main/dashboard.html', context)

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'main/customer_list.html', {'customers': customers})

@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'main/customer_detail.html', {'customer': customer})

@login_required
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'main/customer_form.html', {'form': form})

@login_required
def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id=customer.id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'main/customer_form.html', {'form': form})

@login_required
def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'main/customer_confirm_delete.html', {'customer': customer})

# Repeat similar CRUD views for Service and Subscription
# main/views.py



# Existing customer views...
@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'main/service_list.html', {'services': services})

@login_required
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'main/service_detail.html', {'service': service})

@login_required
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'main/service_form.html', {'form': form})

@login_required
def service_edit(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', service_id=service.id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'main/service_form.html', {'form': form})

@login_required
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'main/service_confirm_delete.html', {'service': service})


# main/views.py

# Existing customer and service views...
@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'main/subscription_list.html', {'subscriptions': subscriptions})

@login_required
def subscription_detail(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    return render(request, 'main/subscription_detail.html', {'subscription': subscription})


@login_required
def subscription_add(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'main/subscription_form.html', {'form': form})


@login_required
def subscription_edit(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('subscription_detail', subscription_id=subscription.id)
    else:
        form = SubscriptionForm(instance=subscription)
    return render(request, 'main/subscription_form.html', {'form': form})


@login_required
def subscription_delete(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'main/subscription_confirm_delete.html', {'subscription': subscription})
