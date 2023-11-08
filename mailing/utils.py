from django.conf import settings
from django.core.cache import cache

from blogs.models import Blog


def get_cache_version_for_article(article_pk):
    if settings.CACHE_ENABLED:
        key = f'article_list{article_pk}'
        article_list = cache.get(key)
        if article_list is None:
            article_list = Blog.objects.filter(article__pk=article_pk)
            cache.set(key, article_list)
    else:
        article_list = Blog.objects.filter(article__pk=article_pk)
    return article_list