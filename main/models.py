from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    status = models.IntegerField(choices=[
        (1, "director"),
        (2, 'manager'),
        (3, 'teachers'),
        (4, 'call center'),
        (5, 'students')
    ], default=1)


class Import_screen(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Info(models.Model):
    logo = models.ImageField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Classroom(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()
    how_many_students = models.CharField(max_length=255)

class Lesson(models.Model):
    name = models.CharField(max_length=255)

class About_education_center(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()


class Blogs_screen(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Blog(models.Model):
    photo = models.ImageField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Give_request(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=255)

class Homeworke(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    page = models.IntegerField()
    numer = models.CharField(max_length=255)

class Courses(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)


class Success_of_our_students(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField()
    text = models.TextField()

class Send_email(models.Model):
    email = models.EmailField()

class Main_office(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    information = models.CharField(max_length=255)

class Info_about_student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    tel_numer_parent = models.CharField(max_length=255)
    


