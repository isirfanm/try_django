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

Install Django package.

```bash
pip install Django==2.0.7
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

# make a new migration
# after make a new migration, you can run command migrate
python manage.py makemigrations
Migrations for 'products':
  products/migrations/0001_initial.py
    - Create model Product

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

Django Apps.

```bash
# create new app
python manage.py startapp products
```

Add app to the Django project.

```python
# try_django/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd parties

    # own
    'products', # our products app
]
```

App Models.

```python
# products/models.py
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()

```

Register app models to administration.

```python
# products/admin.py
from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)

```

Django python shell.

```bash
python manage.py shell
Python 3.8.13 (default, Apr  5 2022, 08:51:40) 
[Clang 13.1.6 (clang-1316.0.21.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> Product
<class 'products.models.Product'>
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>]>
>>> Product.objects.create(title='New product 2', description='another one', price='999', summary='sweet')
<Product: Product object (2)>
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>
>>> obj = Product.objects.get(id=1)
>>> dir(obj)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'description', 'featured', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'objects', 'pk', 'prepare_database_save', 'price', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'summary', 'title', 'unique_error_message', 'validate_unique']
>>> obj.title
'Product 1'

```