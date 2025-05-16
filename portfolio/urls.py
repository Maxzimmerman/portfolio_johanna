from django.urls import path, reverse
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("dienstleistung/<slug:slug>", views.ServiceDetailView.as_view(), name="service-detail"),
    path("impressum", views.Impressum.as_view(), name="impressum"),
    path("datenschutzerklärung", views.DataProtection.as_view(), name="data-protection"),
    path("zertifikate", views.Certificates.as_view(), name="certificates"),
    path("pdf", views.PDFView.as_view(), name="pdf"),
]
