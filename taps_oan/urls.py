from django.conf.urls import url
from taps_oan import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_pub/$', views.add_pub, name='add_pub'),
    url(r'^pub/(?P<pub_name_slug>[\w\-]+)/$', 
        views.show_pub, name='show_pub'),
	url(r'^pub/(?P<pub_name_slug>[\w\-]+)/add_beer/$', 
        views.add_beer, name='add_beer'),
    url(r'^register/$',
        views.register,name='register'),
    url(r'^login/$', 
        views.user_login, name='login'),
	url(r'^logout/$', 
        views.user_logout, name='logout'),
]