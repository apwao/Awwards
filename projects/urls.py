from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url(r'^upload_project/$', views.upload_project, name='upload_project'),
    url(r'^view_projects/$', views.view_projects, name='view_projects'),
    url(r'^single_project/(\d+)/', views.single_project, name='single_project'),
    url(r'^search/', views.search, name='search'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
