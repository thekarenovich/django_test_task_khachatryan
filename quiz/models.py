from django.db import models


class QuizQuestion(models.Model):
    question_id = models.IntegerField(unique=True)
    question_text = models.TextField()
    answer_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
