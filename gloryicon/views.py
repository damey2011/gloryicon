from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from blog.models import StandAloneImageUpload, BlogPost
from blog.serializers import BlogPostSerializer


class Home(View):
    def get(self, request):
        posts = BlogPost.objects.all()[:3]
        return render(request, 'index.html', {'posts': posts})


class LastThreePosts(ListAPIView):
    queryset = BlogPost.objects.all()[:3]
    serializer_class = BlogPostSerializer

@csrf_exempt
def upload(request):
    # folder = 'uploads'

    # uploaded_filename = request.FILES['image'].name
    uploaded_file = request.FILES['upload']

    to_be_uploaded = StandAloneImageUpload()
    to_be_uploaded.image = uploaded_file

    to_be_uploaded.save()
    image_url = to_be_uploaded.image.url

    # return JsonResponse(image_url, safe=False)

    return JsonResponse({'uploaded': 1, 'fileName': to_be_uploaded.image.name, 'url': image_url})
