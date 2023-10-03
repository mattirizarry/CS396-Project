from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, CreateDiscussionPostForm, CreateDiscussionCommentForm
from .models import Course, DiscussionPost, DiscussionComment

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

def create_comment(request, post_id):

    if request.method == "POST":

        post = DiscussionPost.objects.get(id=post_id)
        form = CreateDiscussionCommentForm(request.POST)

        if form.is_valid():
            user = request.user

            created_comment = form.save(commit=False)
            created_comment.user = user
            created_comment.post = post
            created_comment.save()

            return redirect("index")

    form = CreateDiscussionCommentForm()
    context = {
        "form": form,
    }

    return render(request, "dashboard/create_comment.html", context)



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


    
