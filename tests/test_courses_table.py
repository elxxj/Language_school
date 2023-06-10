import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_courses_table_page_template():
    """Test sprawdza, czy strona courses_table wyświetla szablon 'courses_table.html'."""
    client = Client()
    response = client.get(reverse('courses_table'))
    assert response.status_code == 200
    assert 'courses_table.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_courses_table_page_status_code():
    """Test sprawdza, czy kod statusu odpowiedzi HTTP wynosi 200, czyli, że żądanie zakończyło się pomyślnie."""
    client = Client()
    response = client.get(reverse('courses_table'))
    assert response.status_code == 200
