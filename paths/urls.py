from django.conf.urls.static import static
from django.conf import settings
from .views import path as pathV
from .views import course as courseV
from django.urls import path

app_name = 'paths'


urlpatterns = [
    path('', pathV.PathListView.as_view(), name='index'),
    path('add_path/', pathV.PathCreate.as_view(), name='add_path'),
    path('my_paths/', pathV.my_PathsListView.as_view(), name='my_paths'),
    path('courses/', courseV.CourseListView.as_view(), name='courses'),
    path('<slug:slug>/', pathV.PathDetailView.as_view(), name='show_path'),
    path('<slug:slug>/edit/', pathV.PathUpdate.as_view(), name='edit_path'),
    path('<slug:slug>/delete/', pathV.PathDelete.as_view(), name='delete_path'),
    path('<slug:slug>/add_course', courseV.CourseCreateForPath.as_view(), name='course_for_path'),
    path('author/<slug:slug>/', pathV.AuthorPathsListView.as_view(), name='author_paths'),

    path('courses/add_course/', courseV.CourseCreate.as_view(), name='add_course'),
    path('courses/my_courses/', courseV.my_CoursesListView.as_view(), name='my_courses'),
    path('courses/<slug:slug>', courseV.CourseDetailView.as_view(), name='show_course'),
    path('courses/<slug:slug>/edit/', courseV.CourseUpdate.as_view(), name='edit_course'),
    path('courses/<slug:slug>/delete/', courseV.CourseDelete.as_view(), name='delete_couse'),
    path('courses/author/<slug:slug>/', courseV.AuthorCoursesListView.as_view(), name='my_courses'),



    #url('^', include('django.contrib.auth.urls')),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)