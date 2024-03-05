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