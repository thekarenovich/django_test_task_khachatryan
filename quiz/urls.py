from django.urls import path
from .views import create_quiz_question

urlpatterns = [
    path('create_quiz_question/', create_quiz_question, name='create_quiz_question'),
]
