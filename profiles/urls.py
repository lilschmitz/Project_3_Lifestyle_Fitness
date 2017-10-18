from django.conf.urls import url
from .views import profile, no_profile, missing_profile




urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^create/$', no_profile, name='no_profile'),
    url(r'^update/$', missing_profile, name='missing_profile'),

]


