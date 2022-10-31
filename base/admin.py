from django.contrib import admin

# Register your models here.
from .models import Service,Client

# Register your models here.
admin.site.register(Service)
admin.site.register(Client)