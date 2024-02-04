from django.shortcuts import render
from django.views import View
from .models import Home

# Create your views here.

class HomeView(View):
    def get(self, request):
        home = Home.objects.first()

        context = {"home": home}

        return render(request, "portfolio/home.html", context=context)
