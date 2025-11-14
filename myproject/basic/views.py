from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse('helloworld')

def sample1(request):
    return HttpResponse('welcome to jango')    

def sampleInfo(request):
   # data={"name":"ramu","age":22}  
   data=[1,2,3]  
    return JsonResponse(data,Safe=False)

def dynamicResponse(request):
    name=request.GET.get("name",'')
    return HttpResponse(f"hello {name}")
