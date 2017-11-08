from django.conf.urls import url
from contacts.views import contact_list, contact_detailed

urlpatterns = [
    url(r'^$', contact_list, name='contacts'),
    url(r'^(?P<id>\d+)/', contact_detailed, name='contact_details'),
]