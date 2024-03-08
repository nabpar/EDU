from django.urls import path
from .import views



urlpatterns = [
    path('ret/<int:pk>/',views.StudentCourse.as_view(),name = "retrive data"),
    path('courses/all/',views.MY_CourseVIews.as_view(),name = 'all courses view in student dashbord'),
    # path('student/dashbord/',views.StudentDashbord.as_view(),name = 'student_dashbord'),
]