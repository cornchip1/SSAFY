from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm
from django.http import Http404
# Create your views here.

def index(request):
    chats = Chat.objects.all()
    context = {
        'chats':chats
    }
    return render(request,'chattings/index.html',context)

def create(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
        return redirect('chattings:detail',chat.pk)       
    else: 
        form = ChatForm()
    context = {'form':form}
    return render(request,'chattings/create.html',context)    

def detail(request,pk):
    try: 
        chat = Chat.objects.get(pk=pk)
    except Chat.DoesNotExist:
        raise Http404('Does not Exist')
    context = {'chat':chat}
    return render(request,'chattings/detail.html',context)

def delete(request,pk):
    try: 
        chat = Chat.objects.get(pk=pk)
    except Chat.DoesNotExist:
        raise Http404('Does not Exist')
    chat.delete()
    return redirect('chattings:index')