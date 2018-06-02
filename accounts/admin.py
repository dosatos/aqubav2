from django.contrib import admin
from .models import CustomUser#, Progress


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',)


# @admin.register(Progress)
# class ProgressAdmin(admin.ModelAdmin):
#     list_display = ('user',
#                     'question',
#                     'answer',
#                     'correct',
#                     'time_spent',
#                     'time_started')