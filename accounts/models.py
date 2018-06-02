from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
# from lessons.models import Question, Answer


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=45, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=45)
    second_name = models.CharField(max_length=45)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    # progress = models.ForeignKey(Progress, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    # use managers
    # def get_progress(self, date_start, date_end):
    #     return self.progress.


# class Progress(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     correct = models.BooleanField()
#     time_spent = models.DurationField()
#     time_started = models.DateTimeField()
#     time_finished = models.DateTimeField(auto_now_add=True)
