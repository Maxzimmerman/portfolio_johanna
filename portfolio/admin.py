from django.contrib import admin
from .models import Home, Header, HeaderLinks

# Register your models here.

admin.site.register(Home)
admin.site.register(HeaderLinks)
admin.site.register(Header)
