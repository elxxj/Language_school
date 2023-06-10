import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_page_status_code():
    """Test sprawdza, czy kod statusu odpowiedzi HTTP wynosi 200, czyli, że żądanie zakończyło się pomyślnie."""
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_page_template():
    """Test sprawdza, czy strona wyświetla szablon 'profile.html'."""
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert 'profile.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_page_content():
    """Test sprawdza, czy strona profile jest dla zalogowanego użytkownika i czy zawiera nazwę użytkownika"""
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert user.username in response.content.decode()
