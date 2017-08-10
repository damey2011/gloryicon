from django.conf.urls import url
from RCFSFA import views

urlpatterns=[
    url(r'^$', views.RcfHome.as_view(), name='rcf_home')
]