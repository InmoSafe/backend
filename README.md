# backend
.venv\Scripts\activate
source .venv/Scripts/activate
pip freeze > requirements.txt
py manage.py runserver
py manage.py migrate
