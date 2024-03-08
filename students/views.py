from django.shortcuts import render
from .models import My_Course
from rest_framework import generics
from .serializer import My_Course_Serializer
from rest_framework.views import APIView
from rest_framework import response

# Create your views here.

class StudentCourse(generics.RetrieveUpdateDestroyAPIView):
    # user = My_Course.objects.get(id = id)
    serializer_class = My_Course_Serializer

    def get_queryset(self):
        # stu = My_Course.objects.all()
        # user = My_Course.objects.get(user)
        user = self.request.user
        if user.is_authenticated:
            if user.is_student:
                return My_Course.objects.filter(user=user)
            else:
                return My_Course.objects.none()
            

        else:
            return My_Course.objects.none()    
      
  
class MY_CourseVIews(generics.ListAPIView):
    queryset = My_Course.objects.all()
    serializer_class = My_Course_Serializer



# class MY_CourseVIews(generics.CreateAPIView):
#     queryset =My_Course.objects.all()
#     serializer_class = My_Course_Serializer
    


# class MY_CourseVIews(generics.DestroyAPIView):
#     queryset = My_Course.objects.all()
#     serializer_class = My_Course_Serializer


# class StudentDashbord(APIView):
#     def get(self,request):
#         return response({'msg':'this is student dashbord'})    

# from students.models import Emrollment


# enrollments = Emrollment.objects.all()