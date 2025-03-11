from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task

# Create your views here.
""" these functionalities take care of CRUD :-) """

def task_list(request):
    """ this function collects the task items
    """
    # [] empty list is a default if tasks are empty
    # tasks = request.session.get('tasks', [])
    #fetching tasks from DB
    tasks = Task.objects.all()
    # the render function returns a .html template
    return render(request, 'todolistapp/task_list.html', {"tasks" : tasks})
def add_task(request):
    """add new task to db table"""
    if request.method == "POST":
        title = request.POST.get('task')
        #save to db
        if title:
            Task.objects.create(title=title)
    return redirect('task_list')




# def add_task(request):
#     """ this function adds a new task"""
#     if request.method == "POST":
#         task = request.POST.get("task")
#         # checking if task has been captured
#         if task:
#             #fetch the exiting files
#             tasks = request.session.get('tasks', [])
#             # add the new task to above list
#             tasks.append({'task': task, 'done': False})
#             # save the new list to the current session
#             request.session['tasks'] = tasks
#             #notify user
#             messages.success(request, 'Task added successfully')
#         else:
#             messages.error(request, 'Task not added')
#      # redirect is different from render , render loads the template , redirect simply changes the web address to a given location
#     return redirect('task_list')

def delete_task(request, task_id):
    """delete task from db table"""
    Task.objects.filter(id=task_id).delete()
    return redirect('task_list')

# def delete_task(request, index):
#     """ delete the task at the given index"""
#     tasks = request.session.get('tasks', [])
#     if 0 <= index < len(tasks):
#         del tasks[index]
#         #save the new task
#         request.session['tasks'] = tasks
#         messages.success(request, 'Task deleted successfully')
#     else:
#         messages.error(request, 'Task not deleted')
#     return redirect('task_list')

def mark_complete(request, task_id):
    """mark a field as complete in the db"""
    task = Task.objects.get(id=task_id)
    task.complete = True
    task.save()
    return redirect('task_list')

# def mark_complete(request, index):
#         """ mark the task at the given index as complete """
#         tasks = request.session.get('tasks', [])
#         if 0 <= index < len(tasks):
#             tasks[index]['done'] = True
#             request.session['tasks'] = tasks
#             messages.success(request, 'Task marked as complete')
#         else:
#             messages.error(request, 'Task not found')
#         return redirect('task_list')



















