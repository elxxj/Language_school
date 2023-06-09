import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_contact_page_status_code():
    client = Client()
    response = client.get(reverse('contact'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_page_template():
    client = Client()
    response = client.get(reverse('contact'))
    assert response.status_code == 200
    assert 'contact.html' in [t.name for t in response.templates]
