from django.contrib import admin

# Register your models here.
from SolarDB.models import *

admin.site.register(leaseProperty)
admin.site.register(salesProperty)
admin.site.register(User)