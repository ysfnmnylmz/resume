from django.conf.urls import url
from .views import blog_detail

app_name = 'blog'

urlpatterns = [
    url(r'(?P<page_slug>[\w-]+)-(?P<page_id>\d+)', blog_detail, name='blog_detail'),
]
