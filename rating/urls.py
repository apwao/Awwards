from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns=[
    
    url(r'^rate_form/(\d+)/',views.rate_form, name='rate_form'),
    url(r'^rate_project/(\d+)/',views.rate_project, name='rate_project'),
]