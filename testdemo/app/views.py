from django.shortcuts import render
from django.http import HttpResponse
from .models import Record
from django.http import JsonResponse
# Create your views here.

def index(request):
    a = Record.objects.all()
    return render(request,'index.html',{'data':a});

def disp(request):
    id = []
    name = []
    pan = []
    age = []
    gender = []
    email = []
    city = []
    users_list = []
    a = Record.objects.all()
    for i in a:
        id.append(i.id)
        name.append(i.name)
        pan.append(i.pan)
        age.append(i.age)
        gender.append(i.gender)
        email.append(i.email)
        city.append(i.city)

    users_list.append(id)
    users_list.append(name)
    users_list.append(pan)
    users_list.append(age)
    users_list.append(gender)
    users_list.append(email)
    users_list.append(city)

    # print(users_list[0][0])
    return JsonResponse(users_list, safe=False)

def home1(request):
    return render(request,'home.html');

# def add_record(request):
#     name = request.POST['name'];
#     pan = request.POST['panno'];
#     age = request.POST['age']
#     gender = request.POST['gender']
#     email = request.POST['email']
#     city = request.POST['city']
#
#     record = Record.objects.filter(pan=pan)
#     if (record):
#         print("Mached")
#         return HttpResponse("<script> alert('Pan number is already exist..!'); location.href='/'; </script>")
#     else:
#         vRecord = Record(name=name,age=age,pan=pan,gender=gender ,email=email, city=city)
#         vRecord.save()
#         return HttpResponse("<script> alert('Your Record Successfully Added..!'); location.href='/'; </script>")

    # demo for POST METHOD AJAX -> NOT WORKING
# def add_record(request):
#     name = request.POST['info[0]'];
#     pan = request.POST['info[1]'];
#     age = request.POST['info[2]']
#     gender = request.POST['info[3]']
#     email = request.POST['info[4]']
#     city = request.POST['info[5]']
#
#     record = Record.objects.filter(pan=pan)
#     if (record):
#         print("Mached")
#         return HttpResponse("<script> alert('Pan number is already exist..!'); </script>")
#     else:
#         vRecord = Record(name=name,age=age,pan=pan,gender=gender ,email=email, city=city)
#         vRecord.save()
#         return HttpResponse("<script> alert('Your Record Successfully Added..!'); </script>")

def add_record(request):
    name = request.GET['name']
    pan = request.GET['id']
    age = request.GET['age']
    gender = request.GET['email']
    email = request.GET['gender']
    city = request.GET['city']

    record = Record.objects.filter(pan=pan)
    if (record):
        print("Mached")
        return HttpResponse("<script> alert('Pan number is already exist..!'); </script>")
    else:
        vRecord = Record(name=name,age=age,pan=pan,gender=gender ,email=email, city=city)
        vRecord.save()
        return HttpResponse("<script> alert('Your Record Successfully Added..!'); </script>")


def update_record(request):
    print("Update Record Page")
    # id=request.GET['data']
    # a = Record.objects.filter(id=id)
    # return render(request,'update.html',{'data':a})

    id=request.GET['data']

    a = Record.objects.filter(id=id)
    users_list = []
    # users_list.append("Radha");
    for i in a:
        users_list.append(i.id);
        users_list.append(i.name);
        users_list.append(i.pan);
        users_list.append(i.age);
        users_list.append(i.gender);
        users_list.append(i.email);
        users_list.append(i.city);



    # print(users_list)
    # print(a.gender)

    # for i in a:
    #     users_list = append(a[i]);

    # print(length(users_list))

    return JsonResponse(users_list, safe=False)
    # return JsonResponse(users_list, safe=False)
    # return JsonResponse([1, 2, 3, 4], safe=False)
    # return JsonResponse({'data1':a})
    # return render(request,'update.html',{'data1':a})



def update_record_save(request):
    # id= request.POST['id'];
    # name = request.POST['name'];
    # pan = request.POST['panno'];
    # age = request.POST['age']
    # gender = request.POST['gender']
    # email = request.POST['email']
    # city = request.POST['city']
    id= request.GET['id'];
    name = request.GET['name'];
    pan = request.GET['panno'];
    age = request.GET['age']
    gender = request.GET['gender']
    email = request.GET['email']
    city = request.GET['city']

    a = Record.objects.get(id=id)
    a.name = name
    a.pan = pan
    a.age = age
    a.gender = gender
    a.email = email
    a.city = city
    a.save()
    return HttpResponse("<script> alert('Your Record Successfully Updated..!'); </script>")
    # return HttpResponse("<script> alert('Your Record Successfully Updated..!'); location.href='/'; </script>")

def Delete(request):

    # id = request.GET['data']
    # record = Record.objects.get(id=id).delete()
    # return HttpResponse("<script> alert('Your Record Successfully Delete..!'); location.href='/'; </script>")

    id = request.GET['data']
    record = Record.objects.get(id=id).delete()
    return HttpResponse("<script> alert('Your Record Successfully Delete..!');  </script>")

    # id = request.POST['data']
    # record = Record.objects.get(id=id).delete()
    # return HttpResponse("<script> alert('Your Record Successfully Delete..!');  </script>")


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
