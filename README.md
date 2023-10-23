### Как запустить проект
Склонированить репозиторий
'''
https://github.com/FULLLIFE4rever/UserAPI
'''

Создать файл .env в папке с файлом docker-compose.yml
'''
POSTGRES_USER={{ Пользователь БД }}
POSTGRES_PASSWORD={{ Пароль пользователя БД }}
POSTGRES_DB={{ Имя базы данных }}
DB_HOST={{ Имя хоста }}
DB_PORT={{ Порт БД }}
'''

Запустить docker compose в папке проекта
'''
sudo docker compose up -d
'''

### Работа с проектом

Адрес добавления новых вопросов:
http://localhost:8000/add/{число вопросов на добаление}

response:
'''
[
   {
    'question_id': {id вопроса},
    'text':{текст вопроса},
    'answer':{ответ на вопрос}
   }, ... 
]
'''

Список всех вопросов в БД:
http://localhost:8000/all

response:
'''
[
   {
    'question_id': {id вопроса},
    'text':{текст вопроса},
    'answer':{ответ на вопрос}
   }, ... 
]
'''

Поиск по id в БД:
http://localhost:8000/{id вопроса}

response:
'''
{
  'question_id': {id вопроса},
  'text':{текст вопроса},
  'answer':{ответ на вопрос}
}
'''

# Об авторе
Зубарев Александр Владимирович
