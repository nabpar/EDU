from django.contrib import admin
from .models import My_Course
# Register your models here.


@ admin.register(My_Course)
class My_Course_Admin(admin.ModelAdmin):
    list_display = ['id','user','is_student','my_course','paid','date']

