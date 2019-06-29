from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url(r'^upload_project/$', views.upload_project, name='upload_project')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
