from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import (Home, Header, HeaderLinks,
                     Service, AboutUs, SocialIcons,
                     Contact, Footer)
from django.views.generic import ListView, DetailView


# Create your views here.

class HomeView(View):
    template_name = 'portfolio/home.html'

    def get(self, request):
        home = Home.objects.first()
        headers = Header.objects.prefetch_related('links')
        services = Service.objects.all()
        abouts = AboutUs.objects.prefetch_related('icons')
        contact = Contact.objects.prefetch_related('icons', 'forms')
        footer = Footer.objects.first()

        context = {"home": home,
                   "headers": headers,
                   "services": services,
                   "about_list": abouts,
                   "contacts": contact,
                   "footer": footer
                   }

        result = Service.objects.get(pk=1)
        print(result)

        return render(request, self.template_name, context)


class ServiceDetailView(DetailView):
    template_name = 'portfolio/service-detail.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['headers'] = Header.objects.prefetch_related('links')
        context['footer'] = Footer.objects.first()
        return context
