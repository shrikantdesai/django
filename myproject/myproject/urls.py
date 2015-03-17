from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^coverage/', 'myapp.views.coverage'),
    url(r'^test/', 'myapp.views.test'),
    url(r'^import', 'myapp.views.index'),
    url(r'^gmailContacts/$', views.contacts_list),
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
