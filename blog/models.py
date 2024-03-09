from django.db import models

from admins.models import Category
from django.utils.text import slugify

from tinymce.models import HTMLField   # this is  for tinymce

# Create your models here.


def Blog_File(instance, filename):
    return "image/{filename}".format(filename=filename)


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="data_from_category"
    )
    content = HTMLField()
    image = models.ImageField(upload_to=Blog_File, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, null=True, blank=True)


    def save(self,*args,**krgs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.slug = slugify(self.slug)
        super(Blog,self).save(*args,**krgs)    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="Resourceuploader_from_blog",
        null=True,
    )
    # upload_file = models.FilePathField()
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return '%s - %s' %(self.Blog.title, self.name)
