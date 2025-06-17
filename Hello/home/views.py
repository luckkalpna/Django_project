from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context = {
    'variable1': "Hello",
    'variable2': "Welcome"
  }
  # return HttpResponse("this is an home page")
  return render(request, 'index.html', context)

def about(request):
  # return HttpResponse("this is an about page")
  return render(request, 'about.html')

def services(request):
  # return HttpResponse("this is an services page")
  return render(request, 'services.html')

def contact(request):
  # return HttpResponse("this is an contact page")
  return render(request, 'contact.html')
