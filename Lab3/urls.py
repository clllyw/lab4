from django.conf.urls import patterns,url
#from library import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'library.views.home'),
    url(r'^add/$', 'library.views.add'),
    url(r'^add_author/$', 'library.views.add_author'),
    url(r'^retrieve/$', 'library.views.retrieve'),
    url(r'^search/$', 'library.views.search'),
    url(r'^delete/$', 'library.views.delete'),
    url(r'^update/$', 'library.views.update'),
#    (r'^retrieve/$', views.retrieve),   
#    (r'^search/$', views.search),
#    (r'^delete/$', views.delete),
#    (r'^update/$', views.update),
#    url(r'^admin/', include(admin.site.urls)),
)
