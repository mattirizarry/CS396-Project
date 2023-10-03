from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, CreateDiscussionPostForm
from .models import Course, DiscussionPost

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    enrolled_courses = Course.objects.filter(students=request.user)

    # sorted by most recent
    discussions = DiscussionPost.objects.all().order_by("-created_date")

    return render(request, "index.html", {"enrolled_courses": enrolled_courses, "discussions": discussions })

def create_discussion_post(request):
    if request.method == "POST":
        form = CreateDiscussionPostForm(request.POST)

        if form.is_valid():
            user = request.user

            created_post = form.save(commit=False)
            created_post.user = user
            created_post.save()

            return redirect("index")
        
    form = CreateDiscussionPostForm()
    context = {
        "form": form,
    }

    return render(request, "dashboard/create_discussion_post.html", context)

def register(request):
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
    
    form = RegistrationForm()
    context = {
        "form": form,
    }

    return render(request, "registration/register.html", context)


    
