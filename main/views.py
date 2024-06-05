from django.shortcuts import render
from django.http import HttpResponse
from .tasks import slow_func


# def slow_func(a):
#     for i in range(a):
#         print(i, " ---> ", i * 2)

def index(request):
    slow_func.delay(12345)
    # slow_func(20001)
    return HttpResponse("Site is working...")