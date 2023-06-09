import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_home_page_template():
    client = Client()
    response = client.get(reverse('home'))
    assert 'home.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_home_page_returns_response():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200
