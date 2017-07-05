from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.contact_list, name='contacts'),
    url(r'^(?P<id>\d+)/', views.contact_detailed, name='contact_details'),
]