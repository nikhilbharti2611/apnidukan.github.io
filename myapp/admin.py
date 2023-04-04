from django.contrib import admin
from myapp.models import register
from myapp.models import additems

# Register your models here.
admin.site.register(register)
admin.site.register(additems)