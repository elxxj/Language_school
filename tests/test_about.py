import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_about_page_template():
    """ Test sprawdza, czy strona about wyświetla szablon 'about.html'."""
    client = Client()
    response = client.get(reverse('about'))
    assert response.status_code == 200
    assert 'about.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_about_page_contains_text():
    """ Test sprawdza, czy strona about zawiera tekst 'O nas'."""
    client = Client()
    response = client.get(reverse('about'))
    assert response.status_code == 200
    assert "O nas" in response.content.decode()
