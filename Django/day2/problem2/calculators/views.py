from django.shortcuts import render

# Create your views here.
def calculator(request,n1,n2):
    subtracted = n1-n2
    multiplied = n1*n2
    if n2 != 0 : divided = n1/n2
    else: divided = None
    context = {
        'n1':n1,
        'n2':n2,
        'subtracted':subtracted,
        'multiplied':multiplied,
        'divided':divided
    }
    return render(request, 'calculators/calculator.html',context)