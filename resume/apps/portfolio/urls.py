from django.conf.urls import url
from .views import portfolio_detail

app_name = 'portfolio'

urlpatterns = [
    url(r'(?P<page_slug>[\w-]+)-(?P<page_id>\d+)', portfolio_detail, name='portfolio_detail'),
]
