from django.views.generic import TemplateView
from posts.models import Post


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


class TermsView(TemplateView):
    template_name = "pages/terms.html"


class PrivacyView(TemplateView):
    template_name = "pages/privacy.html"


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.all()
        return context
