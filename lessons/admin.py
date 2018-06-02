from django.contrib import admin

from .models import Question, Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'content', 'correct')
    list_display = ('content', 'question', 'correct')


admin.site.register(Question)
# admin.site.register(Answer, AnswerAdmin)