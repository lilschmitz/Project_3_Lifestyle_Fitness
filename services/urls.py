from django.conf.urls import url
from .views import all_services, services_detail, successful_purchase

urlpatterns = [
    # url(r'^$', all_services, name='services'),
    url(r'^services/$', all_services, name='all_services'),
    url(r'^services/(?P<id>\d+)/$', services_detail, name='services_detail'),
    url(r'^success/$', successful_purchase, name='successful_purchase')
]