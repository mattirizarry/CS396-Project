from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/register/", views.register, name="register"),
    path("posts/create/", views.create_discussion_post, name="create_discussion_post"),
    path("posts/<int:post_id>/comment/", views.create_comment, name="create_comment"),
]