from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .file_upload import Uploader
from .models import Category,Subject,Syllabus

 
# Register your models here.

class Admin_Category(admin.ModelAdmin):
    list_display = ['id','name','date_created','date_updated','slug']
admin.site.register(Category,Admin_Category)    

class Admin_Subject(admin.ModelAdmin):
     list_display = ['id','name','date_created','date_updated','code']

#      def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
#              if db_field.name == 'subject':
#                    category_id = request.POST.get(Category)
#                    if category_id:
#                          kwargs['queryset'] =Subject.objects.filter(category_id=category_id)
#                    else:
#                          kwargs['queryset']=Subject.objects.filter.none()

#              return super().formfield_for_foreignkey(db_field, request, **kwargs)
   
admin.site.register(Subject,Admin_Subject)


# class Admin_Topic(admin.ModelAdmin):
#        list_display = ['id','name','date_created','date_updated']

#        def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
#              if db_field.name =='subject':
#                    category_id = request.POST.get('category')
#                    if category_id:
#                          kwargs['queryset']= Subject.objects.filter(category_id=category_id)
#                    else:
#                          kwargs['queryset']= Subject.objects.none()      
#              return super().formfield_for_foreignkey(db_field, request, **kwargs)

# admin.site.register(Topic,Admin_Topic)       


# class Admin_Subtopic(admin.ModelAdmin):
#        list_display = ['id','name','category','subject','topic','date_created','date_updated','slug']
       
#        def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
#              if db_field.name== 'subject':
#                    category_id = request.POST.get('category')
#                    if category_id:
#                          kwargs['queryset'] = Subject.objects.filter(category_id=category_id)
#                    else:     
#                          kwargs['queryset']= Subject.objects.none()
#              elif db_field.name == 'topic':
#                subject_id = request.POST.get('subject')
#                if subject_id:
#                      kwargs['queryset'] = Topic.objects.filter(subject_id=subject_id)
#                else:
#                      kwargs['queryset'] = Topic.objects.none()            
#              return super().formfield_for_foreignkey(db_field, request, **kwargs)
           
# admin.site.register(Subtopic,Admin_Subtopic)       


class Admin_Syllabus(admin.ModelAdmin):
       list_display = ['id','name','category','subject','syllabus_file','date_created','date_updated']

admin.site.register(Syllabus,Admin_Syllabus)       



class Admin_Uploader(admin.ModelAdmin):
       list_display = ['category','category_image','subject','subject_image','subject_files','date_created','date_updated']
       def formfield_for_foreignkey(self, db_field, request,**kwargs):
             if db_field.name == 'subject':
                   category_id = request.POST.get('category')
                   if category_id:
                         kwargs['queryset'] =Subject.objects.filter(category_id=category_id)
                   else:
                         kwargs['queryset']=Subject.objects.none()
                    

             return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Uploader,Admin_Uploader)       