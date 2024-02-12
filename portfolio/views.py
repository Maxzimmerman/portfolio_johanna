from django.shortcuts import render, get_object_or_404
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
        result = Service.objects.get(pk=1)
        print(result)

        return render(request, self.template_name, context)


class ServiceDetailView(DetailView):
    template_name = 'portfolio/service-detail.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.object.service.get(pk=self.kwargs['pk'])
        return context
