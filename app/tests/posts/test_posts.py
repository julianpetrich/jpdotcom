import pytest
from posts.models import Post


@pytest.mark.django_db
def test_posts_model():
    post1 = Post(title="title_1", description_long="description")
    post1.save()
    post2 = Post(title="title_2", description_long="description", cover="test.png")
    post2.save()
    assert Post.objects.all().count() == 2
    assert post1.title == "title_1"
    assert post1.description_long == "description"
    assert post1.cover == "project.png"
    assert post2.cover == "test.png"
    assert str(post1) == post1.title
