from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import QuizQuestion


@csrf_exempt
def create_quiz_question(request):
    if request.method == 'POST':
        data = request.POST
        questions_num = data.get('questions_num')
        if questions_num:
            questions = []
            while len(questions) < int(questions_num):
                response = requests.get('https://jservice.io/api/random?count=1')
                data = response.json()[0]
                question_id = data['id']
                existing_question = QuizQuestion.objects.filter(question_id=question_id).first()
                if existing_question:
                    questions.append(existing_question)
                else:
                    question = QuizQuestion(
                        question_id=question_id,
                        question_text=data['question'],
                        answer_text=data['answer']
                    )
                    question.save()
                    questions.append(question)
            response_data = [
                {'question_id': q.question_id, 'question_text': q.question_text, 'answer_text': q.answer_text,
                 'created_date': q.created_date} for q in questions]
            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse({'error': 'Invalid input'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
