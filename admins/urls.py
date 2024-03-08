from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import Create_Category_View,List_Category_view,Update_Category_View,Delete_Category_View,List_Syllabus_view
from . import views





# router = DefaultRouter()
# router.register(r'uploader/',views.Uploader,basename="uploader")

urlpatterns = [
    # For search
    path('search_categorys/',views.SearchCategory.as_view(),name = "CategorySearch"),

    
    # For Category
    path('create_categorys/',views.Create_Category_View.as_view(),name="reate_Category"),
    path('view_categorys/',views.List_Category_view.as_view(),name="category_view"),
    path('update_categorys/<int:pk>/',views.Update_Category_View.as_view(),name="Update_Category"),
    path('delete_categorys/<int:pk>/',views.Delete_Category_View.as_view(),name="Delete_Category"),

    # For Subject
    path('category_subjects',views.Create_Subject_View.as_view(),name="Create_Subject"),
    path('view_subjects/',views.List_Subject_view.as_view(),name="List_subject"),
    path('view_subjects/<int:pk>/',views.Get_Subject_View.as_view(),name="Get_subject"),
    path('update_subjects/<int:pk>/',views.Update_Subject_View.as_view(),name="Update_Subject"),
    path('delete_subjects/<int:pk>/',views.Delete_Subject_View.as_view(),name="Delete_Subject"),


 # For Syllabus
    path('create_syllabus/',views.Create_Syllabus_View.as_view(),name="Create_Syllabus"),
    path('view_syllabus/',views.List_Syllabus_view.as_view(),name="Syllabus_View"),
    path('update_syllabus/<int:pk>/',views.Update_Syllabus_View.as_view(),name="Update_Syllabus"),
    path('delete_syllabus/<int:pk>/',views.Delete_Syllabus_View.as_view(),name="Delete_Syllabus"),


   ## for uploader
#    path('uploader/',include(router.urls)), 
   path('view_files/',views.Uploader_ListFiles.as_view(),name="view files"),
   path('create_files/',views.Uploader_CreateFiles.as_view(),name="create files"),
   path('update_files/<int:pk>/',views.Uploader_UpdateFiles.as_view(),name="update files"),
   path('delete_files/<int:pk>/',views.Uploader_DeleteFiles.as_view(),name="delete files"),

   #For Contact
   path('contact/',views.ContactView.as_view(),name='contact'),
   path('contact/<int:pk>/',views.SingleContactView.as_view(),name='contact_single'),



]
