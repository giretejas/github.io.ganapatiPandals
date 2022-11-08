from django.contrib import admin
from .models import logins,login,me

# Register your models here.
admin.site.register(logins)
admin.site.register(login)
admin.site.register(me)