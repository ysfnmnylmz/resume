from django.conf.urls import url
from .views import blog_detail, blog_posts

app_name = 'blog'

urlpatterns = [
    url('list/', blog_posts, name='blog_list'),
    url(r'(?P<page_slug>[\w-]+)-(?P<page_id>\d+)', blog_detail, name='blog_detail'),
]
