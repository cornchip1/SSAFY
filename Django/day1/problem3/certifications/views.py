from django.shortcuts import render
from random import randrange, choice

# Create your views here.
def certification1(request):
    name = '김밥'
    age = randrange(25,31)
    grade = choice(['a','b','c','d','s']).upper()
    context = {
        'name':name,
        'age':age,
        'grade':grade,
    }
    return render(request,'certifications/certification1.html', context)

def certification2(request):
    name = '초밥'
    age = randrange(25,31)
    grade = choice(['a','b','c','d','s']).upper()
    context = {
        'name':name,
        'age':age,
        'grade':grade,
    }
    return render(request,'certifications/certification2.html', context)

def certification3(request):
    name = '양념갈비'
    age = randrange(25,31)
    grade = choice(['a','b','c','d','s']).upper()
    context = {
        'name':name,
        'age':age,
        'grade':grade,
    }
    return render(request,'certifications/certification3.html', context)
