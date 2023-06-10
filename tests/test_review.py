import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_about_page_status_code():
    """Test sprawdza, czy kod statusu odpowiedzi HTTP wynosi 200, czyli, że żądanie zakończyło się pomyślnie."""
    client = Client()
    response = client.get(reverse('review'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_about_page_template():
    """Test sprawdza, czy strona review wyświetla szablon 'review.html'."""
    client = Client()
    response = client.get(reverse('review'))
    assert response.status_code == 200
    assert 'review.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_review_page_content():
    """Test sprawdza, czy strona review jest dostepna dla zalogowanego użytkownika i czy zawiera napis 'Opinie'."""
    client = Client()
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('review'))
    assert response.status_code == 200
    assert 'Opinie' in response.content.decode()
