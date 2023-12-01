from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, CreateDiscussionPostForm, CreateDiscussionCommentForm
from .models import Course, DiscussionPost, DiscussionComment, Assignment, Lesson, MultipleChoiceQuestion, Submission, Profile, SubmissionAnswer

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

    course_dict = {}

    for course in courses:

        assignments = Assignment.objects.filter(course=course)

        assignment_dict = {}

        for assignment in assignments:

            students = Profile.objects.filter(courses=course)

            student_dict = {}

            for student in students:

                submissions = Submission.objects.filter(assignment=assignment, user=student)

                submission_dict = {}

                for submission in submissions:
                    
                    submission_answers = SubmissionAnswer.objects.filter(submission=submission)

                    submission_dict[submission.id] = {
                        'submission': submission,
                        'answers': submission_answers
                    }

                student_dict[student.username] = submission_dict

            assignment_dict[assignment.name] = student_dict

        course_dict[course.name] = assignment_dict


    context = {
        'course_dict': course_dict
    }

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

    # check to see if the user has already submitted more than their limit of submissions

    for assignment in assignments:

        submissions = Submission.objects.filter(assignment=assignment, user=request.user)

        if len(submissions) >= assignment.attempts:
            assignments = assignments.exclude(id=assignment.id)

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
    submissions = Submission.objects.filter(assignment=assignment_id, user=request.user)

    if (request.method == "POST"):
        earned = 0
        possible = 0

        if (len(submissions) >= assignment.attempts):
            return redirect("view_course", course_id)

        submission = Submission(assignment=assignment, user=request.user, course=course)
        submission.save()

        for question in questions:
            possible += question.points
            submission_answer = SubmissionAnswer(submission=submission, question=question, answer=request.POST.get(question.question))
            submission_answer.possible = question.points

            if (question.answer == request.POST.get(question.question)):
                earned += question.points
                submission_answer.points = question.points
            
            submission_answer.save()
            
        submission.earned = earned
        submission.possible = possible

        submission.save()

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

        # Compute student grade
        course_grade = 0
        course_possible = 0 

        for assignment in course_assignments:
            assignment_submissions = course_submissions.filter(assignment=assignment)            
            
            submission_answer_dict = {}

            print(f'Assignment {assignment}')

            # Get best score from submissions of assignment

            best_submission = assignment_submissions.order_by('-earned').first()

            course_grade += best_submission.earned * assignment.weight
            course_possible += best_submission.possible * assignment.weight

            print(f'Earned {best_submission.earned} / {best_submission.possible}')

            for submission in assignment_submissions:
                submission_answers = SubmissionAnswer.objects.filter(submission=submission)

                submission_answer_dict[submission.id] = {
                    'submission': submission,
                    'answers': submission_answers
                }

            assignment_dict[assignment.name] = submission_answer_dict

        print(f'Grade for {course.name}: {course_grade} / {course_possible}')

        submission_dict[course.name] = {
            'assignments': assignment_dict,
            'course_grade': course_grade,
            'course_possible': course_possible
        }

    context = {
        'submission_dict': submission_dict,
    }

    print(context)

    return render(request, "report.html", context)