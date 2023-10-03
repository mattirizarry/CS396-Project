from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/register/", views.register, name="register"),
    path("posts/create/", views.create_discussion_post, name="create_discussion_post"),
    path("courses/", views.view_courses, name="view_courses"),
    path("courses/<int:course_id>", views.view_course, name="view_course"),
    path("discussions/<int:discussion_id>", views.view_discussion, name="view_discussion"),
]