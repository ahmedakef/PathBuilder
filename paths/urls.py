from django.conf.urls import include,url

from . import views

app_name = 'paths'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^add_path/$', views.add_path, name='add_path'),
    url(r'^add_course/$', views.add_course, name='add_course'),
    url(r'^paths/(?P<path_id>[0-9]+)/$', views.show_path, name='show_path'),
    url('^', include('django.contrib.auth.urls')),
]
