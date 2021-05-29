import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_home_view(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_template(client):
    response = client.get(reverse("home"))
    assertTemplateUsed(response, "home.html")


@pytest.mark.django_db
def test_home_context(client, create_post):
    create_post()
    response = client.get(reverse("home"))
    assert "post_list" in response.context


@pytest.mark.django_db
def test_about_view(client):
    url = reverse("about")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_view(client):
    url = reverse("contact")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_term_view(client):
    url = reverse("terms")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_privacy_view(client):
    url = reverse("privacy")
    response = client.get(url)
    assert response.status_code == 200
