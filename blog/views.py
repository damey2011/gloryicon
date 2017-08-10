from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from blog.models import BlogPost, Comment, BlogCategory, ContactFormModel


class AllBlogPosts(View):
    def get(self, request):
        category = request.GET.get('category', None)
        if category is not None:
            posts = BlogPost.objects.filter(category__id=category)
        else:
            posts = BlogPost.objects.all()
        paginator = Paginator(posts, 10)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        categories = BlogCategory.objects.all()

        return render(request, 'blog.html', {'posts': posts, 'cat': categories})

    def post(self, request):
        filter_ = request.POST['filter']
        print(filter_)
        if filter_ is not None:
            posts = BlogPost.objects.filter(
                Q(title__icontains=filter_) |
                Q(content__icontains=filter_)
            ).distinct()
        else:
            return redirect('/blogs')

        categories = BlogCategory.objects.all()

        return render(request, 'blog.html', {'posts': posts, 'cat': categories})


class BlogPostView(View):
    def get(self, request, slug):
        bp = BlogPost.objects.get(slug=slug)
        comments = Comment.objects.filter(parent=bp.id)
        bps = BlogPost.objects.all()[:10]
        return render(request, 'blog-single.html', {'post': bp, 'comments': comments, 'bps': bps})


class ComposeBlogPost(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    redirect_field_name = 'r'

    def get(self, request):
        cats = BlogCategory.objects.all()
        return render(request, 'create-post.html', {'cats': cats})

    def post(self, request):
        title = request.POST['post-title']
        content = request.POST['editor1']
        post_image = request.FILES['thumbnail']
        seo_keywords = request.POST['tags']
        seo_desc = request.POST['desc']
        author = request.user
        bp = BlogPost(title=title, content=content, author=author, post_image=post_image, seo_keywords=seo_keywords,
                      seo_desc=seo_desc)
        bp.save()
        cats = BlogCategory.objects.all()
        return render(request, 'create-post.html', {'success_alert': True, 'cats': cats})


class UpdateBlogPost(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    redirect_field_name = 'r'

    def get(self, request, post_id):
        cats = BlogCategory.objects.all()
        post = BlogPost.objects.get(pk=post_id)
        return render(request, 'update-post.html', {'cats': cats, 'post': post})

    def post(self, request, post_id):
        title = request.POST['post-title']
        content = request.POST['editor1']
        bp = BlogPost.objects.get(pk=post_id)
        bp.title = title
        bp.content = content
        bp.save(force_update=True)
        return redirect('/blogs/' + bp.slug, {'success_alert': True})


class SaveComment(View):
    def post(self, request):
        post_slug = request.POST['slug']

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        parent = request.POST['parent']

        c = Comment(name=name, email=email, message=message, parent=parent)
        c.save()

        return redirect('/blogs/' + post_slug, {'comment_added': True})


class Contact(View):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']

        c = ContactFormModel(name=name, email=email, message=message, subject=subject)
        c.save()

        return render(request, 'contact-success.html')
