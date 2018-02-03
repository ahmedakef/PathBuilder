"""PathBuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include


urlpatterns = [
        path('paths/', include('paths.urls')),
        path('admin/', admin.site.urls),
]


from paths.forms import UserCreateForm
from django.views.generic.edit import CreateView


from .views import Register,ActivateAccount,send_activation_keyView


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', Register.as_view(),name='register'),
    path('accounts/register/activate/', ActivateAccount,name='activate'),
    path('accounts/SendActivationKey/', send_activation_keyView,name='SendActivationKeyView'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)