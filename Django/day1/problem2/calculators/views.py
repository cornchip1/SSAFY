from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    sum_result = first + second
    mul_result = first * second
    sub_result = first - second
    try : 
        div_result = first / second
    except ZeroDivisionError :
        div_result = '계산할 수 없습니다.'

    context = {
        'first':first,
        'second':second,
        'sum_result' : sum_result,
        'mul_result' : mul_result,
        'sub_result' : sub_result,
        'div_result' : div_result
    }
    return render(request,'calculators/result.html',context)