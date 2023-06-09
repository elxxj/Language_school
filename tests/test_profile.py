import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_page_status_code():
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_page_template():
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert 'profile.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_page_content():
    client = Client()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert user.username in response.content.decode()
