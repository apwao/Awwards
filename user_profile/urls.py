from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$', views.create_profile, name='create_profile'),
    url('^view_profile/$', views.view_profile, name='view_profile')
]