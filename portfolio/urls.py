from django.urls import path, reverse
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("service/<int:pk>", views.DetailView.as_view(), name="service-detail")
]
