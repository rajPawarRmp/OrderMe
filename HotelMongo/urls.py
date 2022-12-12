
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,include("hotel.urls")),

    # url(r'^media/ ( ?P<path>.* ) $',serve,{'document_root':settings MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
