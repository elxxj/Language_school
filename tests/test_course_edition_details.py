import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_course_edition_details_page_status_code(prepared_data):
    client = Client()
    course_edition = prepared_data['course_edition']
    response = client.get(reverse('course_edition_details', args=[course_edition.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_course_edition_details_page_template(prepared_data):
    client = Client()
    course_edition = prepared_data['course_edition']
    response = client.get(reverse('course_edition_details', args=[course_edition.id]))
    assert response.status_code == 200
    assert 'course_edition_details.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_course_edition_details_page_data(prepared_data):
    client = Client()
    course_edition = prepared_data['course_edition']
    response = client.get(reverse('course_edition_details', args=[course_edition.id]))
    assert response.status_code == 200
    assert response.context['course_edition'] == course_edition
