from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("this is an home page")

def about(request):
  return HttpResponse("this is an about page")

def services(request):
  return HttpResponse("this is an services page")

def contact(request):
  return HttpResponse("this is an contact page")
