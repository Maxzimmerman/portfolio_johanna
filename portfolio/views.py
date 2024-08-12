from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import ContactForm
from django.conf import settings
from django.http import FileResponse, Http404
from django.core.mail import EmailMessage
from .models import (Home, Header, HeaderLinks,
                     Service, AboutUs, SocialIcons,
                     Contact, Footer, TextSection,
                     Imprint)
import logging

logger = logging.getLogger(__name__)


# Create your views here.

class HomeView(View):
    template_name = 'portfolio/home.html'
    form_class = ContactForm
    context = None

    def get(self, request):
        try:
            home = Home.objects.first()
            headers = Header.objects.prefetch_related('links')
            services = Service.objects.all()
            abouts = AboutUs.objects.prefetch_related('icons')
            contact = Contact.objects.prefetch_related('icons', 'forms')
            text = TextSection.objects.first()
            footer = Footer.objects.first()

            self.context = {"home": home,
                            "headers": headers,
                            "services": services,
                            "about_list": abouts,
                            "contacts": contact,
                            "footer": footer,
                            "text": text,
                            "current_page": "home",
                            "form": self.form_class()
                            }

            return render(request, self.template_name, self.context)
        except:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logger.info("Reading Form")
        form = self.form_class(request.POST)
        logger.info("Processing form.")
        if form.is_valid():
            logger.info("Creating Email.")
            cleaned_name = form.cleaned_data['name']
            cleaned_email = form.cleaned_data['email']
            cleaned_service = form.cleaned_data['service']
            cleaned_message = form.cleaned_data['message']

            message = (f"Email von {cleaned_name} ({cleaned_email})"
                       f"\n\nAnliegen: {cleaned_service}"
                       f"\n\n\nNachricht: {cleaned_message}")

            email = EmailMessage(
                "Email von der Website",
                message,
                to=[settings.CONTACT_MAIL],
                from_email=settings.FROM_EMAIL
            )
            logger.info("sending mail")
            email.send()
            logger.info("mail sent.")
            return render(request, "portfolio/partials/success_email.html")
        else:
            logger.warning("form not valid")
        return render(request, self.template_name, self.context)


class ServiceDetailView(DetailView):
    template_name = 'portfolio/service-detail.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.model.objects.get(slug=self.kwargs['slug'])
        context['headers'] = Header.objects.prefetch_related('links')
        context['footer'] = Footer.objects.first()
        context['current_page'] = "other"
        return context


class Impressum(View):
    def get(self, request, *args, **kwargs):
        try:
            headers = Header.objects.prefetch_related('links')
            footer = Footer.objects.first()
            imprint = Imprint.objects.first()

            context = {
                "headers": headers,
                "footer": footer,
                "imprint": imprint,
                "current_page": "other"
            }

            return render(request, "portfolio/impressum.html", context)
        except:
            return render(request, "portfolio/impressum.html")


class DataProtection(View):
    def get(self, request, *args, **kwargs):
        try:
            return FileResponse(open('portfolio_johanna/static/images/data-protection/datenschutzerklarung.pdf', 'rb'),
                                content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()


class Certificates(View):
    def get(self, request, *args, **kwargs):
        try:
            headers = Header.objects.prefetch_related('links')
            footer = Footer.objects.first()

            context = {
                "headers": headers,
                "footer": footer,
                "current_page": "other"
            }
            return render(request, 'portfolio/certificates.html', context)
        except:
            return render(request, 'portfolio/certificates.html')
