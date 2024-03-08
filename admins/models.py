from django.db import models
from .base_class import BaseClass
from django.utils.text import slugify

# Create your models here.
class Category(BaseClass):
    # id = models.IntegerField(primary_key=True)
    slug = models.SlugField(blank=True,null=True)
    class Meta(BaseClass.Meta):
        db_table = "admins_category"


    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        self.slug = slugify(self.slug)
        super(Category,self).save(*args,**kwargs)

    def get_related_subjects(self):
        return self.subjects.all()     
       
            

    def __str__(self):
        return self.name    
  
    

class Subject(BaseClass):
    code = models.IntegerField(unique=True)   
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1) 
    class Meta(BaseClass.Meta):
        db_table = "admins_subject"

    def __str__(self):
        return self.name   
 
    
class Syllabus(BaseClass):
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    syllabus_file=models.FileField(upload_to='syllabus/files',blank=True,null=True)
    

    def __srt__(self):
        return self.name



class ContactLeads(BaseClass):

    class ContactStatus(models.TextChoices):
        RESOLVED='RESOLVED'
        PENDING='PENDING'
        IN_PROGRESS='IN_PROGRESS'
        SPAM='SPAM'

    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField()
    status=models.CharField(max_length=20,choices=ContactStatus.choices,default=ContactStatus.PENDING)
