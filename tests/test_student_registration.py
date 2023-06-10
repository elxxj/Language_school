import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_student_registration_page_status_code():
    """Test sprawdza, czy kod statusu odpowiedzi HTTP wynosi 200, czyli, że żądanie zakończyło się pomyślnie."""
    client = Client()
    response = client.get(reverse('student_registration'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_student_registration_page_template():
    """Test sprawdza, czy strona student_registration wyświetla szablon 'student_registration.html'."""
    client = Client()
    response = client.get(reverse('student_registration'))
    assert response.status_code == 200
    assert 'student_registration.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_student_registration_success():
    """Test sprawdza, czy rejestracja studenta przeszła pomyślnie, czy formularz został przesłany poprawnie"""
    client = Client()
    form_data = {
        'name': 'Anna',
        'surname': 'Kania',
        'username': 'anka',
        'password': 'a1234',
        'confirm_password': 'a1234'
    }
    response = client.post(reverse('student_registration'), form_data)
    assert response.status_code == 302
