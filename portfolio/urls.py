from django.urls import path, reverse
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("service/<int:pk>", views.ServiceDetailView.as_view(), name="service-detail")
]
