from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages,auth

from .models import Todo
from .forms import TodoForm

# Create your views here.


def login(request):

    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if(user!=None):
            auth.login(request,user)
            return redirect('todo')

        else:
            messages.info(request,'Invalid Details !')
            return redirect('/')

    return render(request,'login.html')


def signup(request):

    if(request.method=='POST'):
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']

        if(password==repeatpassword):

            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already taken!')
                return redirect('signup')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email already in use!')
                return redirect('signup')
            
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()

            return redirect('login')
        else:
            messages.info(request,'Password didn\'t match !')
            return redirect('signup')
        
    return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def todo(request):
    if(request.user.is_authenticated):
        userId = request.user.id
        username = request.user.username

    if(request.method=='POST'):
        title = request.POST['title']
        userid = userId 

        todo = Todo.objects.create(title=title,userid=userid)
        todo.save()

        return redirect('todo')
    
    todoList = Todo.objects.filter(userid=userId)

    form = TodoForm()

    context = {
        'userid':userId,
        'username':username,
        'form':form,
        'todolist':todoList,
    }

       
    return render(request,'todo.html' , context)


def edit(request,pk):

    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    context = {
        'form':form
    }

    if(request.method=='POST'):
        title = request.POST.get('title')
        complete = request.POST.get('complete')
        if(title):
            todo.title = title 
        if(complete == 'on'):
            todo.complete = True
        else:
            todo.complete = False 

        todo.save()
        return redirect('todo')


    return render(request,'edit.html',context)



def delete(request,pk):
    if(request.method=='POST'):
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('todo')
    
    return render(request,'delete.html')