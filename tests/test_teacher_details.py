import pytest
from django.test import Client
from django.urls import reverse
from school_app.models import Teacher


@pytest.mark.django_db
def test_teacher_details_page_status_code():
    client = Client()
    response = client.get(reverse('teacher_details'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_teacher_details_page_template():
    client = Client()
    response = client.get(reverse('teacher_details'))
    assert response.status_code == 200
    assert 'teacher_details.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_teacher_details_page_data():
    client = Client()
    teacher = Teacher.objects.create(
        name='Test Teacher',
        surname='Test Surname',
        bio='Test Bio',
        degree='Test Degree'
    )
    response = client.get(reverse('teacher_details'))
    teachers = response.context['teachers']
    assert teacher in teachers
    assert teacher.bio == 'Test Bio'
    assert teacher.degree == 'Test Degree'
