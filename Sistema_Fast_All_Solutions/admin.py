from django.contrib import admin
from .models import ciudad, proveedor, cliente
# Register your models here.
admin.site.register(ciudad)
admin.site.register(proveedor)
admin.site.register(cliente)