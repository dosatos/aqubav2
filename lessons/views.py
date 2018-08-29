import uuid
import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Question, Answer
from accounts.models import Progress


def add_questions(request):
    q1 = Question(title="x + 3 = x",
                  text="Sole for x: x + 3 = x")
    q1.save()
    a11 = Answer(question=q1, content='1, 2', correct=True)
    a11.save()
    a12 = Answer(question=q1, content='0', correct=False)
    a12.save()
    q2 = Question(title="x - 1 = x",
                  text="Sole for x: x + 3 = x")
    q2.save()
    a21 = Answer(question=q2, content='3', correct=True)
    a21.save()
    a22 = Answer(question=q2, content='-3', correct=False)
    a22.save()
    return redirect('/')


def index(request):
    template = "lessons/index.html"
    questions = Question.objects.all()
    args = {"questions": questions}
    return render(request, template, args)


@login_required
def question(request, qid):
    template = "lessons/question.html"
    question = get_object_or_404(Question, qid=qid)
    context = { 'question': question }
    try: # check if this question was approached before
        last_attempt = Progress.objects.filter(user=request.user, question=question).order_by('-time_finished')[0]
    except IndexError: # if not approached
        last_attempt = None
    # process POST request if not approached yet
    if not last_attempt:
        if request.method == 'POST':
            context = validate_answer_choice(request, context)
            return render(request, template, context)
    else:
        context['choice'] = last_attempt.answer
        context['correct'] = last_attempt.correct
    request.session['time_start'] = str(datetime.datetime.now())
    return render(request, template, context)


def validate_answer_choice(request, context):
    """
    This function validates the answer choice, saves the progress history,
    and returns appropriate message in the context

    :return: dict

    """
    question = context['question']
    choice = question.answer_set.get(content=request.POST['choice'])
    time_started = get_time_from_str(request.session['time_start'])
    time_finished = datetime.datetime.now()
    time_spent = (time_finished - time_started).total_seconds()
    correct = True if choice.correct else False
    progress = Progress(user=request.user,
                        question=question,
                        answer=choice,
                        correct=correct,
                        time_spent=time_spent,
                        time_started=time_started,
                        time_finished=time_finished)
    progress.save()
    context['choice'] = choice
    context['correct'] = correct
    return context


# to helper.py
def get_time_from_str(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
