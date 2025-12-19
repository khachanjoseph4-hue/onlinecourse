from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Course, Enrollment, Submission, Choice


@login_required
def submit(request, course_id):
    """
    Handle exam submission:
    - create a Submission
    - associate selected choices
    - redirect to result page
    """
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

    submission = Submission.objects.create(enrollment=enrollment)

    selected_choices = request.POST.getlist('choice')
    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    submission.save()

    return HttpResponseRedirect(
        reverse(
            'onlinecourse:show_exam_result',
            args=(course.id, submission.id)
        )
    )


@login_required
def show_exam_result(request, course_id, submission_id):
    """
    Display exam result with score calculation
    """
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    total_score = submission.get_score()
    possible_score = submission.get_possible_score()

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(request, 'onlinecourse/exam_result.html', context)
