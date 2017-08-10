from rest_framework.serializers import Serializer, ModelSerializer
from blog.models import BlogPost


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content'
        ]