Run below cmd
(venv) apple@apples-MacBook-Air DJANGO % python -m django startproject product_api
(venv) apple@apples-MacBook-Air DJANGO % cd product_api
(venv) apple@apples-MacBook-Air product_api % python manage.py startapp products
In your editor open: product_api/settings.py
Put them at the bottom of the list:
INSTALLED_APPS = [

DATABASES = {
    

open products/models.py use this models.py
python manage.py makemigrations
python manage.py migrate
open products/admin.py use this admin.py
python manage.py createsuperuser fill username, pswrd and emailpython manage.py runserver
python manage.py runserver
started http://127.0.0.1:8000
login with http://127.0.0.1:8000/admin



