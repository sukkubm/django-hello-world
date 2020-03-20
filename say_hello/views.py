from django.shortcuts import render
from .models import Message


def say_hello(request):
    messages = Message.objects.all()
    return render(request, 'hello.html', {'messages': messages})