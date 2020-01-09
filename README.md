# Setting up environment

### install python3

### create a virtual environment (venv) and install django inside it

    $ pip install django
    $ django-admin --version

-----
    
## start making django projects 

    $ mkdir djangoProjects & cd djangoProjects          # djangoProjects
    
    $ django-admin startproject myFirstDjangoProject     
    $ cd myFirstDjangoProject                           # djangoProjects/myFisrtDjangoProject (. or BASE_DIR) 
    
    $ python manage.py runserver                        # starts a server in local machine 127.0.0.1:8000
    open wenbrowser and check url 127.0.0.1:8000

### APP in django                    

    $ python manage.py startapp calc                    # app name = calc
    $ cd calc                                           # ./calc
    create a file 'urls.py' here (write some code)      # ./calc/urls.py
    views.py (write some code)                          # ./calc/views.py
    Add a entry of 'calc urls' to './myFirstDjangoProject/urls.py' (THE MAIN urls.py file of myFirstDjangoProject)
        
#### use concepts of DTL (Django Template Language) for creating dynamic content

    move to BASE_DIR (.)
    $ mkdir templates & cd templates        # ./templates
    make a home.html file                   # ./templates/home.html  
    Add entry in ./myFirstDjangoProject/settings.py > 'Templates DIRS' : [os.path.join(BASE_DIR, 'templates')]
    code ./calc/views.py to render the home.html in browser
    
    For dynamic content: {{}} in 'home.html' and necessary code in 'views.py'
    eg. <h1> hello {{name}} </h1>                              # in home.html
        return render(request,'home.html',{'name': 'Bhola'}    # in views.py home(request) function
   
#### GOOD PRACTICE:
    
    CREATE A ./templates/base.html (a base code common to all pages)
    USE jinja code: {% block content %} {% endblock %} in the body of base.html 
    USE {% extends 'base.html' %} {% block content %} ..some html codes.. {% endblock %} in all the html files
    
##### DEMO PAGE: 
    
    Hello world in django. http://127.0.0.1:8000/
    
    
    