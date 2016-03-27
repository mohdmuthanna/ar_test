from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Examples:
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', 'blog.views.home'),
    url(r'^walli$', 'blog.views.walli'),


    url(r'^admin/', include(admin.site.urls)),
]
