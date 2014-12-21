from django.conf.urls import patterns, url
from quotes import views


urlpatterns = patterns('',
    url(r'^random$', views.random_quote, name='random_quote'),
)