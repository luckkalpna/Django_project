from django.shortcuts import render, redirect
# password for kalpana user: admin***000

# Create your views here.
def index(request):
    # return HttpResponse("Welcome to the Home Page")
    return render(request, 'index.html')

def login(request):
    # return HttpResponse("This is the Login Page")
    return render(request, 'login.html')

def logout(request):
    # return HttpResponse("You have been logged out")
    return render(request, 'logout.html')
