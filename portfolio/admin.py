from django.contrib import admin
from .models import (Home, Header, HeaderLinks, SocialIcons,
                     AboutUs, Service, Contact, Form,
                     SocialIconsContact, Footer, TextSection,
                     Imprint)

# Register your models here.

admin.site.register(Home)
admin.site.register(HeaderLinks)
admin.site.register(Header)
admin.site.register(Service)
admin.site.register(AboutUs)
admin.site.register(SocialIcons)
admin.site.register(Contact)
admin.site.register(Form)
admin.site.register(SocialIconsContact)
admin.site.register(Footer)
admin.site.register(TextSection)
admin.site.register(Imprint)
