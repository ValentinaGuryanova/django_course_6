from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, main

app_name = BlogsConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='view'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)