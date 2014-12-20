from django.conf.urls import patterns, url
from frontend import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]{4}-[0-9]{2}-[0-9]{2})$', views.date_view, name='date_view'),
)