from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Action
from .models import Question
import uuid


def index(request):
    template = "lessons/index.html"
    questions = Question.objects.all()
    args = {"questions": questions}
    return render(request, template, args)


def question(request, qid):
    template = "lessons/question.html"
    question = get_object_or_404(Question, qid=uuid.UUID(qid))
    args = {"question": question,
            "solved": False}
    solved = Action.objects.filter(user_id=request.user.pk).values_list('qid', flat=True)
    if str(question.qid) in solved:
        args['solved'] = True
        args['ans_id'] = Action.objects.get(user_id=request.user.pk,
                                            qid=str(question.qid)).answer_id
    if request.method == "POST":
        correct_answer = question.answer_set.get(correct=True)
        if request.user.is_authenticated:
            ans_content = request.POST['choice_content']
            ans = question.answer_set.get(content=ans_content)
            if ans_content == correct_answer.content:
                args['message'] = 'Correct'
                correct = True
            else:
                args['message'] = 'Incorrect'
                correct = False
            if not str(question.qid) in solved:
                action = Action(
                    user_id=request.user.pk,
                    qid=str(question.qid),
                    answer_id=ans.id,
                    correct=correct)
                action.save()
        else:
            args['message'] = 'Please, authorize first.'
        return redirect('.', args)
    return render(request, template, args)