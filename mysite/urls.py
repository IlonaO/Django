from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^user/', include('apps.users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.blog.urls')),
]
