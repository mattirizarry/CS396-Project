from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/register/", views.register, name="register"),
    path("posts/create/", views.create_discussion_post, name="create_discussion_post"),
    path("posts/<int:post_id>/comment/", views.create_comment, name="create_comment"),
    path("courses/", views.view_courses, name="view_courses"),
    path("courses/<int:course_id>", views.view_course, name="view_course"),
    path("courses/<int:course_id>/lessons/<int:lesson_id>", views.view_lesson, name="view_lesson"),
    path("courses/<int:course_id>/assignments/<int:assignment_id>", views.view_assignment, name="view_assignment"),
    path("discussions/<int:discussion_id>", views.view_discussion, name="view_discussion"),
    path("report", views.report, name="report"),
    path("teacher-report", views.teacher_report, name="teacher_report")
]