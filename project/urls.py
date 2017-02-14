from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include 
from taps_oan import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^taps_oan/', include('taps_oan.urls')),
    # above maps any URLs starting 
    # with taps_oan/ to be handled by
    # the taps_oan application
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)