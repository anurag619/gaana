from django.conf.urls import patterns, url
from play import views

urlpatterns = patterns('',
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^fb', views.fb, name='fb'),

)
