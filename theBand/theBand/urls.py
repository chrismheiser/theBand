from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'theBand.views.home', name='home'),
    url(r'^about/', views.about),
    url(r'^discog/', views.discog),
    url(r'^tourdates/', views.tourdates),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)