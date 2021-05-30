from django.contrib.sitemaps import Sitemap

from posts.models import Post

from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date


class StaticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)
