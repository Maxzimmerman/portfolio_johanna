from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from .models import (Home, Header, HeaderLinks,
                     Service, AboutUs, SocialIcons,
                     Contact, Footer, TextSection)
from django.views.generic import ListView, DetailView
from .forms import ContactForm


# Create your views here.

class HomeView(View):
    template_name = 'portfolio/home.html'
    form_class = ContactForm

    def get(self, request):
        try:
            home = Home.objects.first()
            headers = Header.objects.prefetch_related('links')
            services = Service.objects.all()
            abouts = AboutUs.objects.prefetch_related('icons')
            contact = Contact.objects.prefetch_related('icons', 'forms')
            text = TextSection.objects.first()
            footer = Footer.objects.first()

            context = {"home": home,
                       "headers": headers,
                       "services": services,
                       "about_list": abouts,
                       "contacts": contact,
                       "footer": footer,
                       "text": text,
                       "current_page": "home",
                       "contact_form": self.form_class()
                       }

            return render(request, self.template_name, context)
        except:
            return render(request, self.template_name)


class ServiceDetailView(DetailView):
    template_name = 'portfolio/service-detail.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.model.objects.get(slug=self.kwargs['slug'])
        context['headers'] = Header.objects.prefetch_related('links')
        context['footer'] = Footer.objects.first()
        context['current_page'] = "detail"
        return context


class Impressum(View):
    def get(self, request, *args, **kwargs):
        try:
            home = Home.objects.first()
            headers = Header.objects.prefetch_related('links')
            services = Service.objects.all()
            abouts = AboutUs.objects.prefetch_related('icons')
            contact = Contact.objects.prefetch_related('icons', 'forms')
            text = TextSection.objects.first()
            footer = Footer.objects.first()

            context = {
                       "headers": headers,
                       "footer": footer,
                       }

            return render(request, "portfolio/impressum.html", context)
        except:
            return render(request, "portfolio/impressum.html")
