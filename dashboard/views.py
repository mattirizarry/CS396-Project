from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, CreateDiscussionPostForm, CreateDiscussionCommentForm
from .models import Course, DiscussionPost, DiscussionComment

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    enrolled_courses = Course.objects.filter(students=request.user).order_by("-created_date")[:3]    
    discussions = DiscussionPost.objects.all().order_by("-created_date")

    return render(request, "index.html", {"enrolled_courses": enrolled_courses, "discussions": discussions })

def view_courses(request):
    courses = Course.objects.all()

    context = {
        "courses": courses
    }

    return render(request, "courses.html", context)

def view_course(request, course_id):
    course = Course.objects.get(id=course_id)

    context = {
        "course": course
    }

    print (course)

    return render(request, "course.html", context)

def view_discussion(request, discussion_id):
    discussion = DiscussionPost.objects.get(id=discussion_id)
    # comments = DiscussionComment.objects.(post=discussion_id), copilot do it right for me
    comments = DiscussionComment.objects.filter(post=discussion_id)


    print(comments)

    if request.method == "POST":
        form = CreateDiscussionCommentForm(request.POST)

        if form.is_valid():
            user = request.user

            created_post = form.save(commit=False)
            created_post.user = user
            created_post.save()

            

            return redirect("index")
        
    form = CreateDiscussionCommentForm()

    context = {
        "discussion": discussion,
        "form": form,
        "comments": comments
    }

    return render(request, "discussion.html", context) 

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

    print(post_id)

    if request.method == "POST":

        post = DiscussionPost.objects.get(id=post_id)
        form = CreateDiscussionCommentForm(request.POST)

        print(post.comments.count)

        if form.is_valid():
            user = request.user

            created_comment = form.save(commit=False)
            created_comment.user = user
            created_comment.post = post
            created_comment.save()

            # refresh the page
            return redirect("view_discussion", post_id)
            

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


    
