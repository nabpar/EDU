from rest_framework import serializers

from .models import Blog, Comment

# class BlogView_Serializer(serializers.ModelSerializer):
#     title = serializers.TextField(max_length=255)

#     class Meta:
#         models = Blog
#         fields =
class Search_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        ref_name = 'BlogSearch'

class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'
