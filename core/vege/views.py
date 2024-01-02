from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url= "/user_login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        return redirect('/receipes/')
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)


def delRecipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    # print(queryset)
    return redirect("/receipes/")


def upRecipe(request, id):
    queryset = Receipe.objects.get(id=id)
    context = {'recipe': queryset}

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        queryset.receipe_name = data.get('receipe_name')
        queryset.receipe_description = data.get('receipe_description')
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect("/receipes/")
    return render(request, "update.html", context)


def login_page(request):
     if request.method == "POST":
               username = request.POST['username']
            #    username = "('{}',)".format(username)
               password = request.POST['password']
               # print(User.objects.filter(username=username))
               
               user = authenticate(username = username, password = password)
               if user is None:
                    messages.info(request, "user do not exit. please REGISTER")
                    return redirect('/user_login/')
               else:
                    login(request, user)
                    return redirect('/receipes/')
               
     return render(request, 'login_page.html')
 
def logout_page(request):
    logout(request)
    return redirect('/user_login/')
    


def register_page(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']

            if User.objects.filter(username=username):
                messages.info(
                    request, "Username already exist! Please try some other username.")
                return redirect('/user_register/')

            user = User.objects.create(
                username=username, first_name=first_name, last_name=last_name
            )
            user.set_password(request.POST['password'])
            user.save()
            messages.success(
                request, "Your Account has been created succesfully!!")
            return redirect('/user_register/')
    except:
        pass

    return render(request, 'register_page.html')
