from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .forms import NoteCreationForm, NoteUpdateForm, AccountSettingsForm
from .models import Note

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
    notes = Note.objects.all()
    form = NoteCreationForm()
    
    if request.method == "POST":
        form = NoteCreationForm(request.POST)
        if form.is_valid():
            note_obj = form.save(commit=False)
            note_obj.author = request.user
            note_obj.save()
            return redirect("notes:home")
    context = {
        "notes": notes,
        "form": form
    }
    return render(request, "notes/home.html", context)

def update(request, id):
    updateNote = Note.objects.get(id=id)
    form  = NoteUpdateForm(instance=updateNote)

    if request.method == "POST":
        form = NoteUpdateForm(request.POST)
        if form.is_valid():
            updateNote.title = form.cleaned_data['title']
            updateNote.description = form.cleaned_data['description']
            updateNote.save()
            return redirect("notes:home")

    context = {
        "form": form,
        "note": updateNote
    }

    return render(request, "notes/update.html", context)

def delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect("notes:home")

def settings(request):
    user = request.user
    form = AccountSettingsForm(instance=user)

    if request.method == "POST":
        user.username = request.POST['username']
        user.first_name=request.POST["first_name"]
        user.last_name=request.POST["last_name"]

        user.save()

        messages.success(request,"Account Updated Successfully")

        return redirect("notes:settings")

    context = {
        "form": form,
        "user": user
    }

    return render(request, "notes/settings.html", context)