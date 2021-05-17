import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_posts_view(client):
    url = reverse("post_list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_posts_template(client):
    response = client.get(reverse("post_list"))
    assertTemplateUsed(response, "posts/post_list.html")


@pytest.mark.django_db
def test_posts_context(client, create_post):
    create_post()
    response = client.get(reverse("post_list"))
    assert "post_list" in response.context


@pytest.mark.django_db
def test_post_detail_view(create_post, client):
    post = create_post(title="post_title")
    url = reverse("post_detail", kwargs={"pk": post.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert b"post_title" in response.content


@pytest.mark.django_db
def test_post_detail_template(create_post, client):
    post = create_post(title="post_title")
    url = reverse("post_detail", kwargs={"pk": post.pk})
    response = client.get(url)
    assertTemplateUsed(response, "posts/post_detail.html")


@pytest.mark.django_db
def test_post_detail_context(client, create_post):
    post = create_post(title="post_title")
    url = reverse("post_detail", kwargs={"pk": post.pk})
    response = client.get(url)
    assert "post" in response.context
