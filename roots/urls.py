from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.portraits_list, name='portraits_list'),
    url(r'^portraits/(?P<pk>[0-9]+)/$', views.portraits_detail, name='portraits_detail'),
    url(r'^portraits/new/$', views.portraits_new, name='portraits_new'),
    url(r'^portraits/(?P<pk>[0-9]+)/commentaire/$', views.add_commentaire_to_portraits, name='add_commentaire_to_portraits'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),

    url(r'^profile/$', views.user_detail, name='user_detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^login/$', views.user_login,name='login'),
    url(r'^error/$', views.error,name='error'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
