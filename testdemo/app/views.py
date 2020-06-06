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

    record = Record.objects.filter(pan=pan)
    if (record):
        print("Mached")
        return HttpResponse("<script> alert('Pan number is already exist..!'); location.href='/'; </script>")
    else:
        vRecord = Record(name=name,age=age,pan=pan,gender=gender ,email=email, city=city)
        vRecord.save()
        return HttpResponse("<script> alert('Your Record Successfully Added..!'); location.href='/'; </script>")


def update_record(request):
    print("Update Record Page")
    id=request.GET['data']
    a = Record.objects.filter(id=id)
    return render(request,'update.html',{'data':a})


def update_record_save(request):
    id= request.POST['id'];
    name = request.POST['name'];
    pan = request.POST['panno'];
    age = request.POST['age']
    gender = request.POST['gender']
    email = request.POST['email']
    city = request.POST['city']

    a = Record.objects.get(id=id)
    a.name = name
    a.pan = pan
    a.age = age
    a.gender = gender
    a.email = email
    a.city = city
    a.save()

    return HttpResponse("<script> alert('Your Record Successfully Updated..!'); location.href='/'; </script>")

def Delete(request):
    id = request.GET['data']
    record = Record.objects.get(id=id).delete()
    return HttpResponse("<script> alert('Your Record Successfully Delete..!'); location.href='/'; </script>")


def search(request):
    if "submit" in request.POST:
        fcdata = request.POST['fcf']
        fdata = request.POST['fdata']

        if fcdata == 'name':
            print('name')
            a = Record.objects.filter(name=fdata)
            print(a)
        elif fcdata == 'pan':
            print('pan')
            a = Record.objects.filter(pan=fdata)
            print(a)
        elif fcdata == 'age':
            print('age')
            a = Record.objects.filter(age=fdata)
            print(a)
        elif fcdata == 'gender':
            print('gender')
            a = Record.objects.filter(gender=fdata)
            print(a)
        elif fcdata == 'email':
            print('email')
            a = Record.objects.filter(email=fdata)
            print(a)
        elif fcdata == 'city':
            print('city')
            a = Record.objects.filter(city=fdata)
            print(a)
        else:
            print('Nothing Matched')

    else:
        a = Record.objects.all()

    return render(request,'search.html',{'data':a})
