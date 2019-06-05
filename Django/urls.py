"""StraitsInteractive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from PermissionsBlogSite import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('create_app_form/', views.create_app_form, name='create_app_form'),
    path('create_permission_form/', views.create_app_permission_form, name='create_permission_form'),
    path('view_all_apps/', views.view_all_app, name='view_all_apps'),
    path('view_all_permissions/', views.view_permission, name='view_all_permissions'),
    path('edit/<int:pk>', views.edit_permission, name='edit_permission'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
