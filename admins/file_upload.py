from django.db import models
from .models import Category,Subject

# def CourseFiles(instance,filename):
#     return 'user_{0}/{1}'.format(instance.User.id,filename)

def SubjectFiles(instance,filename):
    return "subjects_files/{filename}".format(filename=filename)


def ImgFile(instance,filename):
    return "imgfiles/{filename}".format(filename=filename)

class Uploader(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=True,
        )
    
    category_image = models.ImageField(upload_to=ImgFile,null=True,blank=True)
    subject_image = models.ImageField(upload_to=ImgFile,null=True,blank=True)
    subject_files = models.FileField(upload_to=SubjectFiles,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.category}-{self.subject}"
    

    def get_subject_by_id(category_id):
        if category_id:
            return Subject.objects.filter(category=category_id)
        else:
            return Subject.objects.filter.none()

