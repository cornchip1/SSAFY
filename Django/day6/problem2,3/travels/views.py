from django.shortcuts import render,redirect,get_object_or_404
from .models import travels
from .forms import TravelForm
# Create your views here.

def index(request):
    Travels = travels.objects.all()
    context = {
        'Travels':Travels
    }
    return render(request,'travels/index.html',context)

def detail(request,pk):
    travel = get_object_or_404(travels,pk=pk)
    context = {
        'travel':travel
    }
    return render(request, 'travels/detail.html',context)

def create(request):
    if request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail',travel.pk)
    else:
        form = TravelForm()
    context = {'form':form}
    return render(request,'travels/create.html',context)

def delete(request,pk):
    travel = get_object_or_404(travels,pk=pk)
    travel.delete()
    return redirect('travels:index')

def update(request,pk):
    travel = get_object_or_404(travels,pk=pk)
    if request.method == "POST":
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail',travel.pk)
    else:
        form = TravelForm(instance=travel)
    context = {'form':form, 'travel':travel}
    return render(request, 'travels/update.html', context)


        