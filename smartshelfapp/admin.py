from django.contrib import admin
from smartshelfapp.models import Employee
from smartshelfapp.models import Shelf
from smartshelfapp.models import Contact
from smartshelfapp.models import Client
from smartshelfapp.models import Customer

# Register your models here.
admin.site.register(Employee)
admin.site.register(Shelf)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Customer)
