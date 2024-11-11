from django.shortcuts import render, redirect
from todo.models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def checkForRegistration(request):
    if request.user.is_authenticated:
        return listTodo(request)
    
    else:
        return signIn(request)

def logIn(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
            
        else:
            return render(request, 'todo/loginForm.html', {'error': 'Invalid username or password'})
    return render(request, 'todo/loginForm.html')

def signIn(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        if User.objects.filter(username=name):
            return render(request, 'todo/signForm.html', {'error':'Username already exist'})

        else:
            user = User.objects.create_user(username=name, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'todo/signForm.html')

def logOut(request):
    logout(request)
    return redirect('/')

def listTodo(request):
    user = request.user
    data = Todo.objects.filter(user=user)    
    return render(request, "todo/index.html", {"data": data})


def add(request):
    if request.method == "POST":
        user = request.user

        title = request.POST.get('title')
        desc = request.POST.get('desc')
        Todo.objects.create(title=title, description=desc, user=user)

        return redirect('/')
    return render(request, "todo/addform.html")

def edit(request, pk):
    obj = Todo.objects.get(id=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        obj.title = title
        obj.description = desc
        obj.save()

        return redirect("/")

    return render(request, "todo/addform.html", {"data":obj})

def delete(request, pk):
        obj = Todo.objects.get(id=pk)
        obj.delete()
        return redirect("/")
        