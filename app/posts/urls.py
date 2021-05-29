from django.urls import path

from .views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug>", PostDetailView.as_view(), name="post_detail"),
]
