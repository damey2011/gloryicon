from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.AllBlogPosts.as_view(), name='all_posts'),
    url(r'compose/', views.ComposeBlogPost.as_view(), name='compose-post'),
    url(r'update/(?P<post_id>\d+)/$', views.UpdateBlogPost.as_view(), name='update-post'),
    url(r'^save-comment/', views.SaveComment.as_view(), name='save-comment'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name='blog-post'),

]