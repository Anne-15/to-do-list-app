from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todoApp.models import TodoList
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    todo_items = TodoList.objects.all().order_by("-added_date")

    return render(request, 'todoApp/index.html',{
        "todo_items": todo_items
    })

@csrf_exempt
def add_item(request):
    current_date = timezone.now()
    content_items = request.POST["content"]
    TodoList.objects.create(added_date = current_date, text = content_items)
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_item(request, todo_id):
    TodoList.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

