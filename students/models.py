from collections.abc import Iterable
from django.db import models
from Accounts.models import  User
from Accounts.profile import Profile
from admins.models import Category,Subject
# Create your models here.





# class StudentProfile(models.Model):
#     user = models.ForeignKey(User,on_delete = models.CASCADE)
#     is_student = models.ForeignKey(User,on_delete = models.CASCADE,blank = True)

class My_Course(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = "student_user")
    is_student = models.BooleanField(default= False)
    my_course = models.ForeignKey(Category, on_delete = models.CASCADE ,blank = True ,related_name = "mycourse")
    # my_subject  = models.ForeignKey(Subject,on_delete = models.CASCADE,blank = True,related_name = "mysubject")


    paid = models.BooleanField(default = False)
    date = models.DateTimeField( auto_now_add = True)


    # def __str__(self):
    #     if self.user:
    #         self.name = self.user.name
    #     return self.name

    def __str__(self):
        return self.user.name
    def __str__(self):
        return f"{self.user} - {self.my_course}"