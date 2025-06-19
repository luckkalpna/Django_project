from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# password for kalpana user: admin***000

# Create your views here.
def index(request):
    # return HttpResponse("Welcome to the Home Page")
    return render(request, 'index.html')

def login(request):
    if request.method=="POST":
        user = authenticate(username=username, password=password)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user is not None:
            return redirect('/')
        # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    # return HttpResponse("This is the Login Page")
    return render(request, 'login.html')

def logout(request):
    # return HttpResponse("You have been logged out")
    return render(request, 'logout.html')
