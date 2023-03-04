from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register),
    path('login/', login_view),
    path('get-user/', get_user),
    path('get-classroom/', get_classrooms),
    path('get-info/', get_info),
    path('create-student/', creat_student),
    path('get-homework/<int:pk>/', get_homework),
    path("get-courses/", get_courses),
    path("get-success/", get_success),
    path('creat-project/', creat_project),
    path('get-projects/', get_projects),
    path('compleated-project/<int:pk>/', compleated_project),
    path('send-email/', send_email),
    path('get-main-office/', get_main_office),
    path('get-info-about-student/', get_info_about_student)
]