from django.db.models import Q,Case, When, Value, IntegerField
from django.db.models.functions import Length

from  rest_framework import generics,filters
from .serializer import Category_Serializer,Subject_Serializer,Syllabus_Serializer,Search_Serializer,Uploader_serializer,Contact_Serializer
from .models import Category,Subject,Syllabus,ContactLeads
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .file_upload import Uploader
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

#Fro searching the category
class SearchCategory(generics.ListAPIView):
    queryset =Category.objects.all()
    serializer_class = Search_Serializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['^name','name']
    OrderingFilter = ['name']



class Create_Category_View(generics.CreateAPIView):
    queryset= Category.objects.all()
    serializer_class = Category_Serializer



class List_Category_view(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class = Category_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["name"]



class Update_Category_View(generics.UpdateAPIView):
    queryset = Category.objects.all()    
    serializer_class = Category_Serializer

class Delete_Category_View(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class =Category_Serializer


# For Subject
class Create_Subject_View(generics.CreateAPIView):
    queryset= Subject.objects.all()
    serializer_class = Subject_Serializer

class Get_Subject_View(generics.RetrieveAPIView):
    queryset=Subject.objects.all()
    serializer_class=Subject_Serializer

class List_Subject_view(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = Subject_Serializer
    filterset_fields = ('category','name')



class Update_Subject_View(generics.UpdateAPIView):
    queryset = Subject.objects.all()    
    serializer_class = Subject_Serializer

class Delete_Subject_View(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = Subject_Serializer






# # For Topic

# class Create_Topic_View(generics.CreateAPIView):
#     queryset= Subject.objects.all()
#     serializer_class = Syllabus_Serializer

# class List_Topic_view(generics.ListAPIView):
#     queryset= Topic.objects.all()
#     serializer_class = Syllabus_Serializer

# class Update_Topic_View(generics.UpdateAPIView):
#     queryset = Topic.objects.all()    
#     serializer_class = Syllabus_Serializer

# class Delete_Topic_View(generics.DestroyAPIView):
#     queryset = Topic.objects.all()
#     serializer_class = Syllabus_Serializer

# # For Sub_Topic

# class Create_Subtopic_View(generics.CreateAPIView):
#     queryset= Subtopic.objects.all()
#     serializer_class = Subtopic_Serializer

# class List_Subtopic_view(generics.ListAPIView):
#     queryset= Subtopic.objects.all()
#     serializer_class =Subtopic_Serializer

# class Update_Subtopic_View(generics.UpdateAPIView):
#     queryset = Subtopic.objects.all()    
#     serializer_class = Subtopic_Serializer

# class Delete_Subtopic_View(generics.DestroyAPIView):
#     queryset = Subtopic.objects.all()
#     serializer_class = Subtopic_Serializer


# For Syllabus


class Create_Syllabus_View(generics.CreateAPIView):
    queryset= Syllabus.objects.all()
    serializer_class = Syllabus_Serializer

class List_Syllabus_view(generics.ListAPIView):
    queryset= Syllabus.objects.all()
    serializer_class =Syllabus_Serializer
    filterset_fields = ('subject',)

class Update_Syllabus_View(generics.UpdateAPIView):
    queryset = Syllabus.objects.all()    
    serializer_class = Syllabus_Serializer

class Delete_Syllabus_View(generics.DestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = Syllabus_Serializer


class Uploader_ListFiles(generics.ListAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer
    filterset_fields = ('category','subject')

class Uploader_CreateFiles(generics.CreateAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer        

class Uploader_UpdateFiles(generics.UpdateAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer            

class Uploader_DeleteFiles(generics.DestroyAPIView):
    queryset = Uploader.objects.all()
    serializer_class = Uploader_serializer


class ContactView(generics.ListCreateAPIView):
    queryset=ContactLeads.objects.all().order_by('-date_created','-date_updated')
    serializer_class=Contact_Serializer 

class SingleContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ContactLeads.objects.all()
    serializer_class=Contact_Serializer               