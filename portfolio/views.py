from django.shortcuts import render
from django.views import View
from .models import Home, Header, HeaderLinks, Service, AboutUs, SocialIcons
from django.views.generic import ListView, DetailView


# Create your views here.

class HomeView(View):
    template_name = 'portfolio/home.html'

    def get(self, request):
        home = Home.objects.first()
        headers = Header.objects.prefetch_related('links')
        services = Service.objects.all()
        abouts = AboutUs.objects.prefetch_related('icons')

        context = {"home": home,
                   "headers": headers,
                   "services": services,
                   "about_list": abouts
                   }

        return render(request, self.template_name, context)
