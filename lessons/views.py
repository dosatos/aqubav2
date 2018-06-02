from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from accounts.models import Progress
import uuid
import datetime


def index(request):
    template = "lessons/index.html"
    questions = Question.objects.all()
    print(questions)
    args = {"questions": questions}
    return render(request, template, args)


def question(request, qid):
    template = "lessons/question.html"
    question = get_object_or_404(Question, qid=qid)
    context = {'question': question}

    if request.method == 'POST':
        if request.user.is_authenticated:
            context = validate_answer_choice(request, question)
            return render(request, template, context)
        else:
            context = {'message': 'Please, authorize first.'}
            return redirect('.', context)
    # non-post method
    request.session.set_expiry(5)
    request.session['time_start'] = str(datetime.datetime.now())
    return render(request, template, context)


def validate_answer_choice(request, question):
    """
    This function validates the answer choice, saves the progress history,
    and returns appropriate message in the context

    :rtype: dict

    """
    # saves progress history
    # generates message if correct
    # cannot solve again if already solved

    choice = question.answer_set.get(content=request.POST['choice'])
    print('--------------------------------------------------------')
    time_started = get_time_from_str(request.session['time_start'])
    print("<<<<<<<<<<<<<<<<", time_started)
    time_finished = datetime.datetime.now()
    time_spent = time_finished - time_started
    correct = True if choice.correct else False
    progress = Progress(question=question,
                        answer=choice,
                        correct=correct,
                        time_spent=time_spent,
                        time_started=time_started,
                        time_finished=time_finished)
    progress.save()
    return {}


# to helper.py
def get_time_from_str(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')