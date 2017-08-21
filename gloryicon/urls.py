"""gloryicon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.models import ContactFormModel, BlogSitemap, StaticPagesSitemap
from blog.views import Contact
from gloryicon import views

sitemaps = {
    'blogs': BlogSitemap,
    'static': StaticPagesSitemap
}

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('blog.urls'), name="blogs"),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^contact/', Contact.as_view(), name="contact"),
    # url(r'^RCFSFA/', include('RCFSFA.urls'), name="rcfsfa"),
    url(r'^curo/', include('curo.urls'), name="curo"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
