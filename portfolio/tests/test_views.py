from http.client import responses
import django.http
import pytest
from django.urls import reverse
from portfolio.views import HomeView, ServiceDetailView, Impressum, DataProtection, Certificates
from .factories import ServiceFactory
from pytest_django.asserts import assertContains

pytestmark = pytest.mark.django_db

@pytest.fixture
def service():
    return ServiceFactory(title="Custom Title", slug="custom-title")


def test_schule_detail_view(rf, service):
    url = reverse("service-detail", kwargs={"slug": service.slug})
    request = rf.get(url)
    callable_obj = ServiceDetailView.as_view()
    response = callable_obj(request, slug=service.slug)
    assertContains(response, service.title)


def test_impressum_success(rf):
    request = rf.get(reverse("impressum"))
    response = Impressum.as_view()(request)
    assert response.status_code == 200


def test_dataprotection_success(rf):
    request = rf.get(reverse("data-protection"))
    response = DataProtection.as_view()(request)
    assert response.status_code == 200


def test_dataprotection_fail(rf):
    request = rf.get(reverse("data-protection"))
    with pytest.raises(django.http.Http404):
        DataProtection.as_view()(request)


def test_certificates_success(rf):
    reqeust = rf.get(reverse("certificates"))
    response = Certificates.as_view()(reqeust)
    assert response.status_code == 200
