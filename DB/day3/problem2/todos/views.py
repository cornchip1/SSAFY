from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request,'todos/index.html',context)


def create(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    
    else:
        form = TodoForm()
    context = {'form':form}
    return render(request,'todos/create.html',context)

def toggle(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        if todo.completed == 1:
            todo.completed = 0
        else:
            todo.completed = 1
        todo.save()
        return redirect('todos:index')

def delete(request,pk):
    if request.method == "POST":
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('todos:index')