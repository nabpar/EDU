from django.contrib import admin

from .models import Blog, Comment

# Register your models here.


class Blog_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "content",
        "image",
        "date_created",
        "date_updated",
        "created_by",
        "slug",
    )

    


admin.site.register(Blog, Blog_Admin)


class Comment_Admin(admin.ModelAdmin):
    list_display = (
        "post",
        "name",
        "body",
        "date_added",
    )


admin.site.register(Comment, Comment_Admin)
