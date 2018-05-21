from django.shortcuts import render, get_object_or_404
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
    args = {"question": question}
    return render(request, template, args)

