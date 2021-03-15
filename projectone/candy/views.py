from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.templatetags.rest_framework import data

from .Serializers import EmployeeSerializers
from .models import Employee, userdetai, trinerdetail


# Create your views here.

@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serialize_data = EmployeeSerializers(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)

    return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getting_data(request):
    record = Employee.objects.all()
    result = EmployeeSerializers(record, many=True)
    return Response(result.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def filter_record(request):
    fil=request.GET.get('name',None)
    record = Employee.objects.filter(name=fil)
    result = EmployeeSerializers(record, many=True)
    return Response(result.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_record(request):
    try:
        record = Employee.objects.get(name='linga')
    except Exception as e:
        print(e)
    result = EmployeeSerializers(record, data =request.data)
    if result.is_valid() :
        result.save()
        return Response(result.data, status=status.HTTP_200_OK)

    return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete_record (request):
    delsoft=request.GET.get('name')
    record=Employee.objects.get(name=delsoft)
    if record:
        print(record)
        record.is_deleted = True
        record.save()
        return Response({"success":"Record Deleted"},status=status.HTTP_200_OK)
    return Response({"Error":"BAD REQUEST"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def curentdelete_dataa(request):

    record=Employee.objects.filter(is_deleted=True)
    result=EmployeeSerializers(record,many=True)
    return Response(result.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def curent_dataa(request):

    record=Employee.objects.filter(is_deleted=False)
    result=EmployeeSerializers(record,many=True)
    return Response(result.data,status=status.HTTP_200_OK)
#new custmor

def home(request):

    print("jfk")
    return render(request, 'startpage.html', {})


def first(request):
    print("lings")
    usernamec = 'trainer'
    passwordc = '12345'
    cu = request.POST.get("Username")
    cp = request.POST.get("password")
    print((cu, cp))
    if cu == usernamec and cp == passwordc:
        return HttpResponseRedirect('/usdeta/')
    return render(request, 'loginuserc.html', {})


def usdeta(request):
    if request.method == 'POST':
        your_name = request.POST['your_name']
        your_password = request.POST['your_password']
        your_email = request.POST['your_email']
        your_role = request.POST['your_role']
        userdetai.objects.create(name=your_name, passwordc=your_password, email=your_email, role=your_role)
        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + your_email + '\n' + your_password + '\n' + your_role
        email = EmailMessage(subject, content, to=[your_email])
        email.send()
        return HttpResponseRedirect('/manipa/')

    return render(request, 'creatinguser.html', {})


def send_mail(request):
    if request.method == 'POST':
        your_name = request.POST['your_name']
        your_password = request.POST['your_mobile_no']
        your_email = request.POST['your_email']
        your_role = request.POST['your_course']

        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + your_password + '\n' + your_email + '\n' + your_role
        email = EmailMessage(subject, content, to=['kutylinga2731@gmail.com'])
        email.send()
        return HttpResponseRedirect('/submit/')

    return render(request, 'stdcreate.html', {})


def manipa(request):
    return render(request, 'startpage.html', {})


# Trainer
def trainerlog(request):
    if request.method == 'POST':
        tu = request.POST.get('Trinername')
        tp = request.POST.get('Trinerpassword')
        record = userdetai.objects.filter(name=tu, passwordc=tp)
        if record:
            print("crazyboy")
            return HttpResponseRedirect('/dahbord/')
        else:
            print("kuty")
    return render(request, 'trilogn.html', {})


def dahbord(request):
    if request.method == 'POST':
        trainer_name = request.POST['Trainer_name']
        course = request.POST['Course']
        student_Name = request.POST['Student_Name']
        duration = request.POST['Duration']
        timeslate = request.POST['Timeslate']
        done = request.POST['yes']
        print(done)
        trinerdetail.objects.create(Trainer_name=trainer_name, Course=course, Student_Name=student_Name,
                                    Duration=duration, Timeslate=timeslate, )
        if done is not None:
            record1 = trinerdetail.objects.all().filter(Trainer_name=trainer_name)
            print(record1)
            return render(request, 'rejister.html', {'StudentInfo': record1})

    return render(request, 'tranerdetail.html', {})


def management(request):
    aname = 'nisar'
    apas = '12345'
    if request.method == 'POST':
        adu = request.POST['mangename']
        adp = request.POST['managepassword']
        print("hello")
        if aname == adu and apas == adp:
            return HttpResponseRedirect('/searcha/')
    return render(request, 'admlogin.html', {})


def searcha(request):
    if request.method == 'POST':
        data = request.POST.get('searchs')
        print(data)
        record2 = {'StudentInfo': trinerdetail.objects.all().filter(Trainer_name=data)}
        return render(request, 'rejister.html', record2)
    return render(request, 'search.html', {})
