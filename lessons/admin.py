from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'qid')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'content', 'correct')
    list_display = ('content', 'question', 'correct')
