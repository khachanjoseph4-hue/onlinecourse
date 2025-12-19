from django.contrib import admin
from .models import Question, Choice
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.apps import apps
from django.db import models

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
