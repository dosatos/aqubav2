from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser


class Action(models.Model):
    user_id = models.IntegerField()
    qid = models.CharField(max_length=64)
    answer_id = models.IntegerField(default=0)
    correct = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # questions_correct = models.ManyToManyField(Question)
    # questions_incorrect = models.ManyToManyField(Question)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.