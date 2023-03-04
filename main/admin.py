from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class Employee(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'status', 'is_active']
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        (_('Personal info'), {'fields':('first_name', 'last_name', 'email')}),
        (_("Permissions"),{
            'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'),{'fields': ('status',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Import_screen)
admin.site.register(Info)
admin.site.register(Classroom)
admin.site.register(Lesson)
admin.site.register(About_education_center)
admin.site.register(Blogs_screen)
admin.site.register(Blog)
admin.site.register(Give_request)
admin.site.register(Homeworke)
admin.site.register(Courses)
admin.site.register(Success_of_our_students)
admin.site.register(Send_email)
admin.site.register(Main_office)
admin.site.register(Info_about_student)