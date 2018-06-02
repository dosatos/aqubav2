from django.contrib import admin
from .models import CustomUser, Progress
from .forms import CustomUserLoginForm


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'question',
                    'answer',
                    'correct',
                    'time_spent',
                    'time_started')
    list_filter = ('user',)
    search_fields = ('user',)
    filter_horizontal = ()