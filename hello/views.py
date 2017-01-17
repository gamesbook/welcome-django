from django.shortcuts import render
from django.http import HttpResponse
from models import Visit


def index(request):
    return HttpResponse("Welcome, World! You're at the 'hello' index. Go to <a href='count'>count</a>?")


def say_hello(request):
    user_agent = request.META['HTTP_USER_AGENT']
    Visit.objects.create(user_agent=user_agent)
    return render(request, 'hello/say_hello.html', {
        'count': Visit.objects.count(),
        'user_agent': user_agent
})
