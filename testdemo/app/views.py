from django.shortcuts import render
from django.http import HttpResponse
from .models import Record

# Create your views here.
def index(request):

    a = Record.objects.all()
    return render(request,'index.html',{'data':a});


def home1(request):
    return render(request,'home.html');

def add_record(request):
    name = request.POST['name'];
    pan = request.POST['panno'];
    age = request.POST['age']
    gender = request.POST['gender']
    email = request.POST['email']
    city = request.POST['city']

    # print(name)
    print(pan)
    record = Record.objects.filter(pan=pan)
    if (record):
        print("Mached")
        return HttpResponse("<script> alert('Pan number is already exist..!'); location.href='/'; </script>")
    else:
        vRecord = Record(name=name,age=age,pan=pan,gender=gender ,email=email, city=city)
        vRecord.save()
        return HttpResponse("<script> alert('Your Record Successfully Added..!'); location.href='/'; </script>")


    # print(age)
    # print(gender)
    # print(email)
    # print(city)


    # vRecord = Record(name=name,age=age,pan=pan,gender=gender ,email=email, city=city)
    # vRecord.save()

    # a = Record.objects.all()

    # return render(request,'index.html',{'data':a});
    # return HttpResponse("<script> alert('Your Record Successfully Added..!'); location.href='/'; </script>")

def update_record(request):
    print("Update Record Page")
    id=request.GET['data']

    # r = Record.objects.get(id=id)

    # print(r.id)
    # print(r[0].pan)

    a = Record.objects.filter(id=id)
    # print(a)


    return render(request,'update.html',{'data':a})


def update_record_save(request):
    id= request.POST['id'];
    name = request.POST['name'];
    pan = request.POST['panno'];
    age = request.POST['age']
    gender = request.POST['gender']
    email = request.POST['email']
    city = request.POST['city']
    # print(id)
    # print(name)
    # print(pan)
    # print(age)
    # print(gender)
    # print(email)
    # print(city)

    a = Record.objects.get(id=id)
    a.name = name
    a.pan = pan
    a.age = age
    a.gender = gender
    a.email = email
    a.city = city
    a.save()

    # b = Record.objects.all()
    # return render(request,'index.html',{'data':b});
    return HttpResponse("<script> alert('Your Record Successfully Updated..!'); location.href='/'; </script>")

def Delete(request):
    id = request.GET['data']
    record = Record.objects.get(id=id).delete()
    return HttpResponse("<script> alert('Your Record Successfully Delete..!'); location.href='/'; </script>")
