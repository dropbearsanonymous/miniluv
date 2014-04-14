from django.conf.urls import patterns, url

from recruit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^accounts/(?P<accountType>\S+)/$', views.accountsList, name='accountsList'),
    url(r'^account/(?P<accountName>\S+)/$', views.account, name='account'),
)
