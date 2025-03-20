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
1. python3 manage.py makemigrations todolistapp appname
2. python3 manage.py migrate
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
3. click the + sign or the prompt to create the data source (for development use sqlite3)

### RELATIONAL DATABASES : DATABASES RELATIONSHIP
1. One to Many Relationship
   -Taskers table (Contains the users who will perform the tasks)
   -Task table (contains the tasks)
To establish a one to many relationship establish a Foreignkey
2. Many to Many

### HOW TO ADD IMAGES (STATIC)
Django uses static directory
Project root directory/ => static/ => images/
Add {% load static %} at the top of the html file
AdD this to settings.py
STATIC



### DJANGO ADMIN
Create a super user for content management purposes
1. Register your models in admin.py
2. Creating a super admin user for the project

python manage.py createsuperuser
3. Visit the link appurl/admin - use the superuser credentials to login

### DJANGO APIs(Application Programming Interface)
Is a set of rules that allows different software apps to communicate with each other

### Think of ana API as a waiter ia a restaurant
1. You(Fronted/client) make an order(request)
2. The waiter(API) takes the request to the kitchen(sever/backend)
3. The kitchen(SERVER) prepares the food(process the request)
4. The waiter(API) brings back the meal (response) to you

### TYPES OT APIS
1. REST API => Uses HTTP methods ::
  - GET :: use this to request data from servers (DEFAULT)
  - POST :: use to save or send data to servers
  - PUT :: use this to update on data on server
  - PATCH:: use this to update only a section of your data
  - DELETE :: USE THIS TO REMOVE DATA FROM YOUR SERVER
2. GraphQL API => Allows clients/fronted to access data only when needed
3. SOAP API => Uses XML methods / older (SECURE)
4. WebSocket API => Enable real data transfer (chat application)

### Steps to create an Api project in DJANGO
1. Install djangorestframework :: pip install djangorestframework
2. Add djangorestframework as part of the installed apps
3. Have views return data as . json files
4. CREATE serializers (picking the data to showcase from the API)
In the app project create a serializers.py

### JSON (JavaScript Object Notation)
This is an interchangeable data format that can be used across any application


###     AUTHENTICATION AND AUTHORIZATION
- Authentication :: IDENTITY MANAGEMENT :: Who is using the app
- Authorization :: USER PRIVILEDGES :: What user can do once authorized

### STEP IN CREATING AUTHENTICATION MODULE
1. Within settings.py of the project modify the authentication settings
  a. LOGIN_URL :: ## redirect unauthenticated users back to the login screen
  b. LOGIN_REDIRECT_URL :: After login what page will the user see
  c. LOGOUT_REDIRECT_URL :: ## After logout, redirect user back to login screen
2. Create views function for the register, login and logout processes
3. Create the rendered/redirected templates
4. Register the urls to map the authentication functions in views
5. Do migrations :: python3 manage.py migrate

### EXTENDING THE DJANGO AUTH USER 
1. I mport the class AbstractUser in our models.py
2. Create the custom user class, name should be customUser
3. Tell djongo to use the custom model for the user
4. Update our forms to also use the custom model
    a. crate a form.py in the app folder, write out our custom user form
5. Update the views functions to use the custom model
6. Updating the templates to reflect the new inputs :: register.html
7. Ensure that our django can handle media
     a. inside settings.py media_url, media_root
     b. urls.py include the media reference as part of te urlpatterns
8. Reset the database and make new migrations 
     - delete the migration.py file in the migration folder
     - Delete the db.sqlite file
     - python3 manage.py makemigrations todolistapp (appname)
     - python3 manage.py migrate
     - 



















FrontEnd(HTML <CSS (web) , Android(Jetpack compose) , React Native ,
Reactjs)
=> middleware => backend (server scripting (python->django), database)

