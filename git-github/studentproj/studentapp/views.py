from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse

def input(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        try:
            if form.is_valid():
                return HttpResponse("data submitted successfully")
        except BaseException:
            return HttpResponse("Error occured")
    else:
        form=NameForm()
        return render(request,'student.html',{'form':form})

# Create your views here.
