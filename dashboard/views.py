from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, CreateDiscussionPostForm, CreateDiscussionCommentForm
from .models import Course, DiscussionPost, DiscussionComment, Assignment, Lesson, MultipleChoiceQuestion, Submission, Profile

# ===========================================
#             /
# ===========================================

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    enrolled_courses = Course.objects.filter(students=request.user)
    instructor_courses = Course.objects.filter(instructor=request.user)

    courses = enrolled_courses.union(instructor_courses).order_by('-created_date')[:3]

    discussions = DiscussionPost.objects.all().order_by("-created_date")

    context = {
        "courses": courses,
        "discussions": discussions
    }

    return render(request, "index.html", context)

# ===========================================
#             /teacher-report
# ===========================================

def teacher_report(request):
    if not request.user.is_authenticated:
        return redirect("login")

    courses = Course.objects.filter(instructor=request.user)
    assignments = Assignment.objects.filter(course__in=courses)
    submissions = Submission.objects.filter(course__in=courses)
    students = Profile.objects.filter(courses__in=courses)

    # create a dictionary following this style dict[coursename][assignmentname] = [submissions]

    submission_dict = {}

    for course in courses:
        course_assignments = assignments.filter(course=course)
        course_submissions = submissions.filter(course=course)

        assignment_dict = {}

        for assignment in course_assignments:

            student_dict = {}

            for student in students:
                student_submissions = course_submissions.filter(user=student)
                max_submission = student_submissions.order_by('-earned').first()
                
                student_dict[student.username] = max_submission
            
            assignment_dict[assignment.name] = student_dict        

        submission_dict[course.name] = assignment_dict

    context = {
        'submission_dict': submission_dict
    }

    print(submission_dict)

    return render(request, "teacher-report.html", context)

# ===========================================
#             /courses
# ===========================================

def view_courses(request):
    # update this to only show courses that the user is enrolled in OR the user is the instructor in
    enrolled_courses = Course.objects.filter(students=request.user)
    instructor_courses = Course.objects.filter(instructor=request.user)

    courses = enrolled_courses.union(instructor_courses)

    context = {
        "courses": courses
    }

    return render(request, "courses.html", context)

# ===========================================
#             /courses/<int:course_id>
# ===========================================

def view_course(request, course_id):
    course = Course.objects.get(id=course_id)
    assignments = Assignment.objects.filter(course=course_id)
    lessons = Lesson.objects.filter(course=course_id)

    context = {
        "course": course,
        'assignments': assignments,
        'lessons': lessons
    }

    return render(request, "course.html", context)

# ===========================================
#            /courses/<int:course_id>/lessons/<int:lesson_id>
# ===========================================

def view_lesson(request, course_id, lesson_id):
    
    lesson = Lesson.objects.get(id=lesson_id, course_id=course_id)

    context = {
        "lesson": lesson
    }

    return render(request, "lesson.html", context)

# ===========================================
#             /courses/<int:course_id>/assignments/<int:assignment_id>
# ===========================================

def view_assignment(request, course_id, assignment_id):

    assignment = Assignment.objects.get(id=assignment_id, course_id=course_id)
    course = Course.objects.get(id=course_id)
    questions = MultipleChoiceQuestion.objects.filter(assignment=assignment_id)

    if (request.method == "POST"):
        earned = 0
        possible = 0

        for question in questions:
            possible += question.points

            if (question.answer == request.POST.get(question.question)):
                earned += question.points

        # create a new submission object and save it to the database
        submission = Submission(earned=earned, possible=possible, assignment=assignment, user=request.user, course=course)
        submission.save()

        # return to the course page
        return redirect("view_course", course_id)

    context = {
        "assignment": assignment,
        "questions": questions
    }

    return render(request, "assignment.html", context)

# ===========================================
#           /discussions/<int:discussion_id>
# ===========================================

def view_discussion(request, discussion_id):
    discussion = DiscussionPost.objects.get(id=discussion_id)
    comments = DiscussionComment.objects.filter(post=discussion_id)
        
    form = CreateDiscussionCommentForm()

    context = {
        "discussion": discussion,
        "form": form,
        "comments": comments
    }

    return render(request, "discussion.html", context) 

# ===========================================
# GET          /discussions/create
# ===========================================

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

# ===========================================
# POST          /discussions/create 
# ===========================================

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

            # refresh the page
            return redirect("view_discussion", post_id)
            
# ===========================================
# GET          /accounts/register
# ===========================================

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

# ===========================================
# GET          /report
# ===========================================

def report(request):
    if not request.user.is_authenticated:
        return redirect("login")

    courses = Course.objects.filter(students=request.user)
    assignments = Assignment.objects.filter(course__in=courses)
    submissions = Submission.objects.filter(user=request.user)

    # create a dictionary following this style dict[coursename][assignmentname] = [submissions]

    submission_dict = {}

    for course in courses:
        course_assignments = assignments.filter(course=course)
        course_submissions = submissions.filter(assignment__in=course_assignments)

        assignment_dict = {}

        for assignment in course_assignments:
            assignment_submissions = course_submissions.filter(assignment=assignment)
            assignment_dict[assignment.name] = list(assignment_submissions)

        submission_dict[course.name] = assignment_dict

    context = {
        'submission_dict': submission_dict
    }

    return render(request, "report.html", context)