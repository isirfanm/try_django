# Try Django

## How to

Setup python environment with `pyenv`. 

```bash
# install python
pyenv install 3.8.13

# create virtualenv
pyenv virtualenv 3.8.13 django

# activate virtualenv
pyenv activate django

# set local virtualenv for this folder
pyenv local django
```

Create blank django project.

```bash
# create django project
django-admin startproject try_django

# go to project folder
cd try_django
```

Run development server

```bash
# run development server
python manage.py runserver
```

Database migration.

```bash
# migrate database
python manage.py migrate
```

Django administration.

```bash
# create super user
python manage.py createsuperuser
Username (leave blank to use 'alo-mohamadirfanislami'): cfe
Email address: 
Password: secretpassword
Password (again): secretpassword
Superuser created successfully.
```

Login to Administration Page on URL : `http://127.0.0.1:8000/admin/login/?next=/admin/`

