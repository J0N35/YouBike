from django.conf.urls import patterns, url

urlpatterns = patterns('bike_status.views',
    url(r'^$', 'status'),
)
