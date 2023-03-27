from django.shortcuts import render
from random import choice

# Create your views here.
def first(request):
    third = request.GET.get('third')
    context = {
        'thirdv':third,
    }
    return render(request,'throw_loops/first.html',context)

def second(request):
    first = request.GET.get('first')
    context = {
        'firstv':first,
    }
    return render(request,'throw_loops/second.html',context)

def third(request):
    v1 = request.GET.get('secondv1')
    v2 = request.GET.get('secondv2')
    choose = choice([v1,v2])
    context = {
        'first':first,
        'chosen':choose
    }
    return render(request,'throw_loops/third.html',context)