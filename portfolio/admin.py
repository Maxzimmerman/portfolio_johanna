from django.contrib import admin
from .models import Home, Header, HeaderLinks, SocialIcons, AboutUs, Service

# Register your models here.

admin.site.register(Home)
admin.site.register(HeaderLinks)
admin.site.register(Header)
admin.site.register(Service)
admin.site.register(AboutUs)
admin.site.register(SocialIcons)
