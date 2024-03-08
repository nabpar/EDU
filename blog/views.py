from django.shortcuts import render
# from django.views import generic
from rest_framework import generics

# from rest_framework.generics import ListAPIView
from .models import Blog, Comment
from .serializer import Blog_Serializer, Comment_serializer,Search_Serializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.db.models import Case, When, Value, CharField

# Create your views here


# For Blog Portion





class SearchList(generics.ListAPIView):
    # lookup_field='title'
    serializer_class = Search_Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title","category__name"]
    ordering_fields = ['title','conten']

    def get_queryset(self):
       search_query  = self.request.query_params.get('search','')
       queryset = Blog.objects.all()

       if search_query:
          
            queryset = queryset.annotate(
            starts_with_search=Case(
                When(title__istartswith=search_query, then=Value(1)),
                default=Value(0),
                output_field=CharField()
        )
    ).order_by('-starts_with_search', 'title')
           
       for backend in self.filter_backends:
        queryset = backend().filter_queryset(self.request,queryset,view=self)
        # print(queryset)
       return queryset
        # serialzer = Search_Serializer(View_Blog,many = True)
#     queryset = Blog.objects.all()
#     serializer_class = Search_Serializer

#     filter_backends = (filters.SearchFilter,)
#     filterset_fields = ["title","category"]
#     search_fields = ["title","^title","category","^catrgory"]
#     ordering_fields = ["category"]


    # def get_queryset(self):
    #     queryset = Blog.objects.all()
    #     title= self.request.query_params.get('title')
    #     if title is not  None:
    #         queryset = queryset.filter(blog_title__icontains=title)
    #         return queryset

    # def get_queryset (self ):
    #     queryset = Blog.objects.all()
    #     print(json.dump(queryset))
    #     title = self.request.query_params.get("title")
    #     if title is not None:
    #         queryset = queryset.filter(blog_title__icontains = title)

    #     return queryset    

        



class View_Blog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer
 
class Retrieve_Blog(generics.RetrieveAPIView):
    queryset=Blog.objects.all()


class Create_Blog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


class Upadate_Blog(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


class Destroy_Blog(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer


# For Resource Uploader


class Create_Comment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment_serializer


class Update_Comment(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment_serializer


class Delete_Comment(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment_serializer


from rest_framework import viewsets


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class =Blog_Serializer