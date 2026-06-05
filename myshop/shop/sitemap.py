from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            'home',
            'team-steel-puma',
            'galery-steel-puma',
            'price-steel-puma',
            'news-steel-puma',
            'rules-steel-puma',
        ]

    def location(self, item):
        return reverse(f"shop:{item}")


