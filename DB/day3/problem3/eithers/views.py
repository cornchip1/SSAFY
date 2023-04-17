from django.shortcuts import render,redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from random import choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions':questions
    }
    return render(request,'eithers/index.html',context)

def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {
        'form':form
    }
    return render(request,'eithers/create.html',context)

def random_page(request):
    page = choice(Question.objects.values_list('pk',flat=True))
    return redirect('eithers:detail',page)

def detail(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {'question':question,'comment_form':comment_form,'comments':comments}
    return render(request,'eithers/detail.html',context)

def comments_create(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment_form.save()
    return redirect('eithers:detail',question_pk)