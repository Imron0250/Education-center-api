from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def creat_student(request):
    user = request.user
    if user.status == 4:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = User.objects.create_user(username=username,email=email,is_superuser=True, status=5)
        u.set_password(password)
        u.save()
        ser = UserSerializer(u)
        return Response(ser.data)
    else:
        return Response("Error")

@api_view(["POST"])
def login_view(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user) 
            data = {
                'success' : True,
                'user' : {
                    "id" : user.id,
                    "username": user.username,
                    'token': token.key,
                }
            }
        else:
            data = {
                "success" : False,
                "error": "User or password error!"
            }
    except Exception as err:
        data = {
            "success": False,
            "error": f'{err}'
        }
    return Response(data)   


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    if user.status == 1:
        user = User.objects.all()
        ser = UserSerializer(user, many=True)
        return Response(ser.data)
    else:
        return Response("Your statuc is not director and you cannot get user")


    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_classrooms(request):
    user = request.user
    if user.status == 1:
        classroom = Classroom.objects.all()
        ser = ClassroomSerializer(classroom, many=True)
        return Response(ser.data)
    else:
        return Response("Your statuc is not director and you cannot get classrooms")
    
@api_view(['GET'])
def get_info(request):
    info = Info.objects.all()
    ser = InfoSerializer(info, many=True)
    return Response(ser.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_homework(request,pk):
    user = request.user
    user = User.objects.get(id=pk)
    if user.status == 5:
        homeworke = Homeworke.objects.filter(student_id=user)
        ser = HomeworkeSerializer(homeworke, many=True)
        return Response(ser.data)
    else:
        return Response("You cannot get homework")
    
@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    ser = CoursesSerializer(courses, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_success(request):
    succsess = Success_of_our_students.objects.all()
    ser = Success_of_our_studentsSerializer(succsess, many=True)
    return Response(ser.data)

    
    
@api_view(['POST'])
def send_email(request):
    email = request.POST.get('email')
    e = Send_email.objects.create(email=email)
    ser = Send_emailSErializer(e)
    return Response(ser.data)


@api_view(['GET'])
def get_main_office(request):
    main_office = Main_office.objects.all()
    ser = Main_officeSerializer(main_office,many=True)
    return Response(ser.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_info_about_student(request):
    user = request.user
    if user.status == 4:
        students_info = Info_about_student.objects.all()
        ser = Info_about_studentSerializer(students_info, many=True)
        return Response(ser.data)
    else:
        return Response('You cannot get students info')

        







