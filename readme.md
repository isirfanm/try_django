# Try Django

## Steps

Setup python environment with `pyenv`. 

```sh
# install python
pyenv install 3.8.13

# create virtualenv
pyenv virtualenv 3.8.13 django

# activate virtualenv
pyenv activate django
```

Create blank django project.

```sh
# create django project
django-admin startproject try_django

# go to project folder
cd try_django

# set local virtualenv for this project
pyenv local django
```

