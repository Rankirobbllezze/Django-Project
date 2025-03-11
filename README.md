##3 To create a django project
django-admin startproject <nameofapplication>

### How to run a django project
python manage.py runserver

### DJANGO PROJECT FILE
1. MANGE.PY :: COMMAND LINE UTILITY allowing us to access django project : entry file
2. todolist/ : this directory is the actual python project
3. __init__.py : this is an empty file that indicates the above directory is a python project
4. asgi.py : an empty file for ASGI compatible web servers to serves to serve your project
5. wsig.py : an empty file for ASGI compatible web servers to serves to serve your project
6. settings.py : settings/configuration file for the django project
7. urls,py : these rl declarations that map to our django app.

### HOW TO CREATE AN APP INSIDE A DJANGO PROJECT
python manage.py startapp <nameofapplication>
### Register the app
- go to settings.py and include the app using the appname

### DJANGO APP FILES
1. MIGRATIONS/ : DATABASE MIGRATION FILES (EMPTY INITIALLY)
2. __init__.py : indicates the app ia a python application
3. admin.py : used to register models for the django admin panel
4. app.py : contains the app configurations
5. models.py : defines the database models (TABLES)
6. tests.py : contains test cases for the app
7. views.py : handles request-response logic (functional/controller)
8. urls.py : (manually created on app level) : define url patterns for the app

### JINJA TEMPLATING
THIS IA SYNTAX USED TO CREATE DJANGO INTERFACES 
-To create templates
 a. Inside the app folder create a template folder
 b. inside the template you can create the .html files , .css, .js
 c. to consolidate the templating for our project, modify the following
   -set up a global templates directory for referencing our templates i.e move the todolist templatas folder to the global perspective i.e root directory level
   -register this change in settings.py for the project under the templates directory settings
          'DIRS': [BASE_DIR / 'templates'], #ADD THIS LINE

### STEPS TO INCLUDE DB PERSISTENCY FOR PROJECTS IN DJANGO
MODELS.PY :converted to db tables by django
After defining our models.py
1. python manage.py makemigrations appname
2. python manage.py migrate
3. 
### DATABASES
Organized collection of data that allows users to store, retrieve update and delete information moore efficiently
### TYPES OF DATABASES
1. Relational Databases
   -store data in tables : rows (records) and columns (fields)
   -tables can be related
   -uses the SQL query language
2. NoSQL Databases
3. In-Memory Databases
### WHY USE DATABASES
1. Persistent data storage 
2. Efficient data retrieval
3. Data relationship
4. Security and integrity

### USING DATABASES IN DJANGO
1. Define our model data
2. Use django migration commands to convert our models into actual database tables
3. Object relational Mappers (ORM'S) to interact with the db using python code instead of raw SQL statements

### TO CONVERT MODELS TO TABLES
1. python manage.py makemigrations appname
2. python manage.py migrate

###STEPS TO AD A DATA SOURCE
1. Double click on the db.sqlite3
2. Or simply from the pycharm selact the database icon
3. click the + sin or the prompt to create the data source (for development use sqlite3)


