from django.urls import path, reverse
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("service/<slug:slug>", views.ServiceDetailView.as_view(), name="service-detail"),
    path("impressum", views.Impressum.as_view(), name="impressum")
]
