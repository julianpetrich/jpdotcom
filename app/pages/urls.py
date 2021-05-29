from django.urls import path

from .views import AboutView, ContactView, HomePageView, PrivacyView, TermsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about"),
    path("contact", ContactView.as_view(), name="contact"),
    path("terms", TermsView.as_view(), name="terms"),
    path("privacy", PrivacyView.as_view(), name="privacy"),
]
