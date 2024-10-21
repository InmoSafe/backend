# backend
.venv\Scripts\activate
pip freeze > requirements.txt
py manage.py runserver
py manage.py migrate
