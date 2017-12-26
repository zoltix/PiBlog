""" django 3.0 qui a du être adaptée"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    
    # Examples:
    # url(r'^$', 'crepes.views.home', name='home'),
    #path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]