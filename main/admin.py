from django.contrib import admin

# Register your models here.
from .models import Customer, Service, Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("customer",)

admin.site.register(Customer)
admin.site.register(Service)
#admin.site.register(Subscription)
admin.site.register(Subscription, SubscriptionAdmin)