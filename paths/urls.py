from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path

app_name = 'paths'


urlpatterns = [
    url(r'^$', views.PathListView.as_view(), name='index'),
    path(r'<slug:slug>/', views.PathDetailView.as_view(), name='show_path'),
    url(r'^add_path/$', views.PathCreate.as_view(), name='add_path'),
    path(r'<slug:slug>/edit/', views.PathUpdate.as_view(), name='edit_path'),
    path(r'<slug:slug>/delete/', views.PathDelete.as_view(), name='delete_path'),
    url(r'^my_paths/$', views.my_PathsListView.as_view(), name='my_paths'),
    path(r'author/<slug:slug>/', views.AuthorPathsListView.as_view(), name='author_paths'),

    url(r'^courses/$', views.CourseListView.as_view(), name='courses'),
    path(r'courses/<slug:slug>', views.CourseDetailView.as_view(), name='show_course'),
    url(r'^courses/add_course/$', views.CourseCreate.as_view(), name='add_course'),
    path(r'courses/<slug:slug>/edit/', views.CourseUpdate.as_view(), name='edit_course'),
    path(r'courses/<slug:slug>/delete/', views.CourseDelete.as_view(), name='delete_couse'),
    url(r'^courses/my_courses/$', views.my_CoursesListView.as_view(), name='my_courses'),
    path(r'courses/author/<slug:slug>/', views.AuthorCoursesListView.as_view(), name='my_courses'),



    #url('^', include('django.contrib.auth.urls')),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)