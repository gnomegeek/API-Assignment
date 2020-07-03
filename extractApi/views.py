from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import NewUser
from django.core import serializers
from django.contrib import messages

import requests


messages = None
def home(request):
    return render(request, 'index.html', {'messages': messages})

def load(request):
    global messages
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    newusers = users.json()
    for user in newusers:
        newUser = NewUser(
            name = user['name'],
            username = user['username'],
            email = user['email'],
            website = user['website'],
            phone = user['phone']
        )

        newUser.save()
    messages = "10 users added to database. Please check admin site."
    return redirect('/')

def dump(request):
    global messages
    NewUser.objects.all().delete()
    redirect('index.html')
    messages = "All Users deleted"
    return redirect('/')

def deleteUser(request):
    global messages
    id = request.POST['userID']
    user = NewUser.objects.filter(id = id)
    if (user.exists()):
        user.delete()
        messages = f'User with ID {id} deleted from database.'
        return redirect('/')
    else:
        messages = "No User Found"
        return redirect('/')

def userInfo(request):
    global messages
    user = NewUser.objects.filter(id = request.POST['userID'])
    
    if(user.exists()):
        print(user)
        # return JsonResponse(, safe=False)
        qs_json = serializers.serialize('json', user)
        return HttpResponse(qs_json, content_type='application/json')
    else:
        messages = "No User Found"
        return redirect('/')

def register(request):
    global messages
    if(request.method == 'POST'):
        user = NewUser(
            name = request.POST['name'],
            username =  request.POST['username'],
            email = request.POST['email'],
            website = request.POST['website'],
            phone = request.POST['phone']
        )

        user.save();
        messages = "User Succesfully Registered"
        return redirect('/')
        
    else:
        return render(request, 'register.html')
