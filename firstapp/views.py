from django.shortcuts import render
from firstapp.models import Stud, Stud2
from django.http import HttpResponse
from firstapp.forms import studentform
# Create your views here.

def home(request):
    student = Stud.objects.all()
    return render(request,'firstapp/index.html',{'stud' : student})

def home2(request):
    return render(request,'firstapp/home.html')

def addstud(request):
    sn = 45
    snm = "Om"
    age = 34
    gmail = 'abc1234@gmail.com'

    s = Stud(sno = sn,sname = snm,age = age,email = gmail)
    s.save()
    return HttpResponse("<h2>Record Inserted Successfully</h2>")

def updatestud(request,myid):
    sn = 8
    snm = "Om"
    age = 80
    gmail = 'abc1234@gmail.com'

    s = Stud(id = myid,sno = sn,sname = snm,age = age,email = gmail)
    s.save()
    return HttpResponse("<h1>Records updated successfully</h1>")

def deletestud(request,myid):
    s = Stud.objects.get(id=myid)
    s.delete()
    return HttpResponse("<h1>Record Deleted</h1>")

def showforms(request):
    if request.method == "POST":
        st = studentform(request.POST)
        if st.is_valid():
            name = st.cleaned_data['sname']
            email = st.cleaned_data['semail']
            st2 = Stud2(snm = name, semail = email)
            st2.save()

    else:
        print("This is get request")
        st = studentform()

    return render(request,'firstapp/home.html',{'so':st})


