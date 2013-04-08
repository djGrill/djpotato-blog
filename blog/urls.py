from django.conf.urls.defaults import *
from django.conf import settings
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, {}, name='index'),
    url(r'^create/$', views.create, {}, name='create'),
    url(r'^edit/(?P<post_id>\d+)/$', views.edit, {}, name='edit'),
    url(r'^delete/(?P<post_id>\d+)/$', views.delete, {}, name='delete'),
    url(r'^(?P<year>\d+)/$', views.archive_year, {}, name='archive_year'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', views.archive_month, {}, name='archive_month'),
    url(r'^\d+/\d+/[\w\-]+/(?P<post_id>\d+)/$', views.details, {}, name='details'),
    # url(r'^__exception_test__/$', views.exception_test, {}),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        )
