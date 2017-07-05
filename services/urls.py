from django.conf.urls import url
from .views import all_services, services_detail

urlpatterns = [
    # url(r'^$', all_services, name='services'),
    url(r'^services/$', all_services, name='all_services'),
    url(r'^services/(?P<id>\d+)/$', services_detail, name='services_detail'),
]