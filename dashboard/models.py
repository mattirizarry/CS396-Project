from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class Profile(AbstractUser):
    pass

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    students = models.ManyToManyField(Profile, related_name='courses', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    assignments = models.ManyToManyField('Assignment', related_name='courses', blank=True)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lessonBody = RichTextField(default='')
    lessonFiles = models.FileField(upload_to='uploads/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class MultipleChoiceQuestion(models.Model):
    question = models.CharField(max_length=100)
    choices = models.TextField()
    answer = models.CharField(max_length=100)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

class Submission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)

class DiscussionPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

class DiscussionComment(models.Model):
    commentBody = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name="comments")