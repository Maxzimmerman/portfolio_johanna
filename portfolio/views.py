from django.shortcuts import render
from django.views import View
from .models import Home, Header, HeaderLinks
from django.views.generic import ListView, DetailView


# Create your views here.

class HomeView(ListView):
    template_name = 'portfolio/home.html'
    model = Home

    def get_queryset(self):
        # Fetch all references with related images, features, and tags
        queryset = super().get_queryset().prefetch_related("links")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
