from django.conf.urls import patterns, url


urlpatterns = patterns(
    'app.views',
    url(r'^$', 'home'),

    url(r'/students/$', 'student_collection'),
    url(r'/students/(?P<pk>[0-9]+)$', 'student_record')
)
