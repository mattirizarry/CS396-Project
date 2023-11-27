from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(DiscussionPost)
admin.site.register(Profile, UserAdmin)
admin.site.register(DiscussionComment)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(Lesson)
admin.site.register(SubmissionAnswer)
