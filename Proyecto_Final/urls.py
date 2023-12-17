"""
URL configuration for Proyecto_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from AppCoder.views import no_hay_nada
from Proyecto_Final import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('AppCoder.urls')),
    path('accounts/', include('accounts.urls')),
    re_path(r'^.*/$', no_hay_nada, name='no_hay_nada'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)