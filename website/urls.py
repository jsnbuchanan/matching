from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),

    url(r'^results', 'match.views.results'),
    url(r'^profiles', 'match.views.profiles'),
    url(r'^profile/(?P<profile_name>[^/]+)/', 'match.views.profile'),
    url(r'^search', 'match.views.home'),
    url(r'^$', 'match.views.home'),
)
