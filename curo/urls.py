from django.conf.urls import url
from curo import views

urlpatterns=[
    url(r'^$', views.CuroHome.as_view(), name='curo_home')
]