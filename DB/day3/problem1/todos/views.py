from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm



# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'todos/index.html',context)

def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {'form':form}
    return render(request,'todos/create.html',context)

# def detail(request,pk):
#     todo = Todo.objects.get(pk=pk)
#     context = {'todo':todo}
#     return render(request,'todos:detail.html',context)

def delete(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')

def complete(request,pk):
    if request.user.is_authenticated :
        todo = get_object_or_404(Todo,pk=pk)
        if todo.check_users.filter(pk = request.user.pk).exists():
            todo.check_users.remove(request.user)
        else:
            todo.check_users.add(request.user)
        return redirect('todos:index')
    return redirect('accounts:login')