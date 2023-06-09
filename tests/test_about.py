import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_about_page_template():
    client = Client()
    response = client.get(reverse('about'))
    assert response.status_code == 200
    assert 'about.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_about_page_contains_text():
    client = Client()
    response = client.get(reverse('about'))
    assert response.status_code == 200
    assert "O nas" in response.content.decode()
