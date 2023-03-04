from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_active']

class Import_screenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Import_screen
        fields = "__all__"

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"

class About_education_centerSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_education_center
        fields = "__all__"

class Blogs_screenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs_screen
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class Give_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Give_request
        fields = "__all__"


class HomeworkeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeworke
        fields = "__all__"

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class Success_of_our_studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Success_of_our_students
        fields = "__all__"

class Send_emailSErializer(serializers.ModelSerializer):
    class Meta:
        model = Send_email
        fields = "__all__"

class Main_officeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_office
        fields = "__all__"

class Info_about_studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info_about_student
        fields = "__all__"

Import_screen
Info
Classroom
Lesson
About_education_center
Blogs_screen
Blog
Give_request
Courses
Success_of_our_students