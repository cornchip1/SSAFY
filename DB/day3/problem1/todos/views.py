from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_form = TodoForm()
    context = {
        'todo_form':todo_form,
    }
    return render(request,'todos/index.html',context)

def create(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo_form = TodoForm(request.POST)
    if todo_form.is_valid():
        task = todo_form.save(commit=False)
        task.todo = todo
        task.save()
    return redirect('todos:index',todo.pk)