from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView

# Create your views here.

def index(request):
    return render(request, "notes/index.html")

def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created successfully!")
            return redirect('notes:login')

    context = {
        "form": form
    }
    return render(request, "notes/register.html", context)

def home(request):
    return render(request, "notes/home.html")