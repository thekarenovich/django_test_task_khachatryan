import json

from django.test import TestCase
from django.urls import reverse


class QuizTestCase(TestCase):
    def test_create_quiz_question(self):
        response = self.client.post(reverse('create_quiz_question'), {'questions_num': 3})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)
