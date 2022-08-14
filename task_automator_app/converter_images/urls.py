from django.urls import path

from . import views

urlpatterns = [
    path('upload_file/', views.model_form_upload, name='model_form_upload'),
    path('show_all_files/', views.show_all_files, name='show_all_files'),
    path('convert_to_png/<str:file_name>', views.convert_to_png, name='convert_to_png'),
    path('delete/<str:file_name>', views.delete_img, name='delete_img')
]