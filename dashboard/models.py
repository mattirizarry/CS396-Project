from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class Profile(AbstractUser):
    role = models.PositiveSmallIntegerField(default=0)
    
class Course(models.Model):
    # Model Attributes
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    assignments = models.ManyToManyField('Assignment', related_name='courses', blank=True)
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    students = models.ManyToManyField(Profile, related_name='courses', blank=True)

    def __str__(self):
        return self.code

class Lesson(models.Model):
    # Model Attributes
    name = models.CharField(max_length=100)
    description = models.TextField()
    lessonBody = RichTextField(default='')
    lessonFiles = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.course.code

class Assignment(models.Model):
    # Model Attributes
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    attempts = models.IntegerField(default=1)

    # Foreign Keys
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.course.code

class MultipleChoiceQuestion(models.Model):
    # Model Attributes
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100, default='')
    option2 = models.CharField(max_length=100, default='')
    option3 = models.CharField(max_length=100, default='')
    option4 = models.CharField(max_length=100, default='')
    answer = models.CharField(max_length=100, default='')
    points = models.IntegerField(default=5)

    # Foreign Keys
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Submission(models.Model):
    # Model Attributes
    created_at = models.DateTimeField(auto_now_add=True)
    earned = models.IntegerField(default=0)
    possible = models.IntegerField(default=0)

    # Foreign Keys
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    
class SubmissionAnswer(models.Model):
    # Model Attributes
    answer = models.CharField(max_length=100, default='')
    points = models.IntegerField(default=0)
    possible = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign Keys
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.question} - {self.points}/{self.possible}'

class DiscussionPost(models.Model):
    # Model Attributes
    title = models.CharField(max_length=100)
    description = RichTextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class DiscussionComment(models.Model):
    # Model Attributes
    commentBody = RichTextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.post.title + " - " + self.user.username