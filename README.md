# Django Веб-Сервис для Викторин

Этот проект представляет собой Django веб-сервис, предоставляющий REST API для создания и получения вопросов для викторин с использованием публичного API.

## Инструкции по сборке и запуску

Следуйте этим инструкциям, чтобы собрать и запустить Docker-образ с нашим веб-сервисом.

### Требования

1. Установленный Docker и Docker Compose.
2. Файл `requirements.txt` для быстрого скачивания необходимых зависимостей.

### Установка зависимостей

1. Убедитесь, что у вас есть файл `requirements.txt` с перечисленными зависимостями.
2. Установите зависимости с помощью `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### Сборка Docker-образа

1. Клонируйте репозиторий проекта:

   ```bash
   git clone https://github.com/thekarenovich/django_test_task_khachatryan.git
   cd django_test_task_khachatryan
   ```

2. Соберите Docker-образ с помощью `docker-compose`:

   ```bash
   docker-compose build
   ```

### Запуск Docker-контейнера

1. Запустите Docker-контейнер:

   ```bash
   docker-compose up
   ```

2. Сервис будет доступен по адресу: http://localhost:8000/

### Пример запроса к POST API

Для создания викторины с 3 вопросами отправьте POST-запрос на `/quiz/create_quiz_question/`:

```http
POST http://localhost:8000/quiz/create_quiz_question/
Content-Type: application/x-www-form-urlencoded

questions_num=3
```

## Используемые технологии

- Django: Python-фреймворк для веб-разработки.
- PostgreSQL: СУБД для хранения данных о вопросах для викторин.
- Zipkin: Инструмент для мониторинга и трассировки запросов.

## Unit-тесты

Проект включает в себя unit-тесты, которые можно запустить с помощью команды:

```bash
python manage.py test quiz
```

## Отправка HTTP-запросов

Для удобства работы с проектом, предоставлен файл `requests.http`, содержащий готовые запросы для HTTP-запросов. Вы можете использовать его с помощью расширения "REST Client" в вашей среде разработки (например, Visual Studio Code) для отправки запросов и проверки функциональности сервиса.

Эти инструкции помогут вам собрать, настроить и запустить проект, а также использовать его API для создания и получения вопросов для викторин.

## Рекомендуется к просмотру

- https://github.com/thekarenovich/improved_web_page_psql

- https://github.com/thekarenovich/business_card

- https://github.com/thekarenovich/Projects

- https://github.com/thekarenovich/Django_REST