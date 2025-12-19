from django.contrib import admin
from .models import Question, Choice, Submission
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade')
    search_fields = ['question_text']


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id',)
