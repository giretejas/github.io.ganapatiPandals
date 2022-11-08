from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
from myapp.models import logins, me


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def test(request):
    return render(request,'test.html')

def visual(request):
    return render(request,'visual.html')

def userregipage(request):
    return render(request,'userregi.html')

def userregi(request):
    if request.method=='POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        role=request.POST.get('role')
        log=logins()
        log.name=name
        log.username=username
        log.password=password
        log.role=role
        log.save()
        return render(request,'index.html', context={'usersavemsg':"user created sucessfully"})
    return render(request,'index.html')

def show(request):
    def empview():
        results=logins.objects.all()
        return results
    return render(request,'show.html',{'res':empview()})

def login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if logins.objects.filter(username=username,password=password).exists():
            loginobj=logins.objects.get(username=username,password=password)
            request.session['userid']=loginobj.id
            role=loginobj.role

            if role=='Admin':
                icdata3 = me.objects.all()
                return render(request, 'adminview.html', context={'data3': icdata3})
                #return render(request,'adminview.html',context={'user':loginobj})
            else:
                return render(request,'newsletter.html',context={'user':loginobj})

        else:

            return render(request,'index.html',context={'msg':'Login failed'})
    else:
        return render(request,'usercreation.html')

def login(request):
    return render(request,'login.html')

def adminview(request):
    icdata3 = me.objects.all()
    return render(request, 'adminview.html', context={'data3': icdata3})
    return render(request,'adminview.html')

def newsletter(request):
    if request.method=='POST':
        return render(request,'newsletter.html')
    return render(request,'login.html')

def mes(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        log=me()
        log.fullname=fullname
        log.email=email
        log.subject=subject
        log.message=message
        log.save()
        return render(request,'index.html', context={'usersavemsg':"user created sucessfully"})
    return render(request,'index.html')

def apm(request):
    icdata3=me.objects.all()
    return render(request,'adminview.html',context={'data3':icdata3})