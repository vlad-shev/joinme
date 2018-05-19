"""joinme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import events.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/create', views.post_create, name='post_create'),
    path('gallery/<int:pk>/show', views.post_show, name='post_show'),
    path('gallery/<int:pk>/update', views.post_update, name='post_update'),
    path('gallery/<int:pk>/delete', views.post_delete, name='post_delete'),
