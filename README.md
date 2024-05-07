## Django Blog
<ol>
    <li>Project Setup</li>
    <li>Application and Routes</li>
    <li>Templates</li>
    <li>Admin Page</li>
    <li>Database and Migrations</li>
    <li>User Registation</li>
    <li>Login and Logout System</li>
    <li>User Profile and Picture</li>
    <li>Update User Profile</li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ol>

## Important Django Commands

1) Starts a new Project
```
django-admin startproject name_project
```

2) Runs the Server
```
python3 manage.py runserver
```

3) Creates an App
```
python3 manage.py startapp app_name
```

4) Prepares Django to make migrations
```
python3 manage.py makemigrations
```

5) Makes the migrations
```
python3 manage.py migrate
```

6) Creates an Admin User
```
python3 manage.py createsuperuser 
```

7) Returns SQL code on the migration
```
python3 manage.py sqlmigrate blog 0001
```

8) Use the Shell
```
python3 manage.py shell
```

## Crispy
1) pip install django_crispy_forms
2) pip install crispy_bootstrap4
3) Add both of these to INSTALLED_APPS:
```
'crispy_forms',
'crispy_bootstrap4',
```
4) Add both of these at the bottom:
```
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
5) Use {% load crispy_forms_tags %} and {{ form|crispy }} in the html file.
