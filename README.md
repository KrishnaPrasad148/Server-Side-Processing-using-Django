# EX05 Server Side Processing – Login System using Django

**Date:** 20/11/2025  

---

## AIM:
To develop a **Server Side Processing (SSP)** web application using **Django**, where the user can log in using a webpage built with HTML and CSS, and the login authentication is processed on the server using Django’s built-in authentication system.


## DESIGN STEPS:

### Step 1:
Create a new Django project.

### Step 2:
Create a new Django app for handling login functionality.


### Step 3:
Add the app to `INSTALLED_APPS`, configure templates, and set up static file paths in `settings.py`.

### Step 4:
Create the HTML login and home pages inside  
`loginapp/templates/loginapp/`.

### Step 5:
Create the CSS file (`login.css`) and place it inside  
`loginapp/static/css/`.

### Step 6:
Implement server-side authentication in `views.py` using  
`authenticate()` and `login()` functions.

### Step 7:
Configure URL routing in both `SSPproject/urls.py` and  
`loginapp/urls.py`.

### Step 8:
Apply migrations.

### Step 9:
Create a Django superuser for login.

### Step 10:
Run the webserver and test the login functionality.



## PROGRAM:
```
Developed By : Krishna Prasad S  
Register No. : 212223230108  
```

### Shell commands:
```
django-admin startproject SSPproject

python manage.py startapp loginapp

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

### views.py:
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "loginapp/login.html")


def home(request):
    return render(request, "loginapp/home.html")

```

## OUTPUT:


## RESULT:

The Server Side Processing (SSP) Login System using Django was successfully developed, executed, and tested.
