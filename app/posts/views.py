from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "post_list"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
