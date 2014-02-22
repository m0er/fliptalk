from django.conf.urls import patterns, include, url
from fliptalk import views, user

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fliptalk.views.home', name='home'),
    # url(r'^fliptalk/', include('fliptalk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', views.index, name='index'),
    url(r'^demo/?$', views.demo, name='demo'),
    
    url(r'^post/?$', views.post, name='post'),

    url(r'^register/email/?$', views.register, name='emailRegister'),
    url(r'^login/email/?$', views.login, name='emailLogin'),
    url(r'^logout/?$', views.logout, name='logout'),
)
