import pytest
from posts.models import Post


@pytest.fixture
def create_post(db):
    def make_post(**kwargs):
        if "title" not in kwargs:
            kwargs["title"] = "title"
        if "slug" not in kwargs:
            kwargs["slug"] = "slug"
        kwargs["description_long"] = "description"
        return Post.objects.create(**kwargs)

    return make_post
