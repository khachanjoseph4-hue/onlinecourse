from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice, Submission

def submit(request):
    if request.method == "POST":
        return HttpResponse("Exam submitted")
    return HttpResponse("Submit page")

def show_exam_result(request):
    return HttpResponse("Congratulations! You passed the exam.")
