from django.db import models
import uuid


IS_CORRECT_CHOICES = (
    (True, 'Correct'),
    (False, 'Incorrect')
)


class Question(models.Model):

    qid = models.UUIDField(default=str(uuid.uuid4()),editable=False)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    correct = models.BooleanField(default=False, choices=IS_CORRECT_CHOICES)

    def __str__(self):
        return self.content