from django.db import models
import uuid


IS_CORRECT_CHOICES = (
    (True, 'Correct'),
    (False, 'Incorrect')
)


class Question(models.Model):

    qid = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    text = models.TextField()

    # def __init__(self, *args, **kwargs):
    #     super(Question, self).__init__(self, *args, **kwargs)
    #     self.qid = str(uuid.uuid4())

    def __str__(self):
        return self.title


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    correct = models.BooleanField(default=False, choices=IS_CORRECT_CHOICES)

    def __str__(self):
        return self.content