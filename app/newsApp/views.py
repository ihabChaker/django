from django.shortcuts import render, HttpResponse,redirect
from .models import News as news,RegistrationData
from .forms import RegistrationForm,RegistrationModal
from django.contrib  import messages
# Create your views here.


def News(request):
    obj=news.objects.get(id=1)
    context={
        'data': obj
    }
    return render(request, "news.html",context)


def Home(request):
    context={
        'name':'white jeff'
    }
    return render(request, "home.html",context)


def Contact(request):
    return render(request, "contact.html")


def News_date(request,year):
    articles= news.objects.filter(pub_date__year=year)
    context={
        'list':articles,
        'year': year
    }
    return render(request,'newsdate.html',context)


def register(request):
    context={
        'form': RegistrationModal
    }
    return render(request,'signup.html',context)


def addUser(request):
    form=RegistrationForm(request.POST)
    if form.is_valid():
        register= RegistrationData(user=form.cleaned_data['user'],
                                   password=form.cleaned_data['password'],
                                   email=form.cleaned_data['email'],
                                   phone=form.cleaned_data['phone'],
                                   )
        register.save()
        messages.add_message(request,messages.SUCCESS,"You have signed up successfuly")
    return redirect('register')


def addUser1(request):
    form=RegistrationModal(request.POST)
    if form.is_valid():
        form.save()

    return redirect('register1')

def register2(request):
    context={
        'form':RegistrationModal
    }
    return render(request,'registermodal.html',context)
