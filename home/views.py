from django.shortcuts import render,redirect

# Create your views here.
from .forms import factorial_form

from .models import factorial_model

from .tasks import Factorial

from django.http import HttpResponse


def factorial(request):
    form=factorial_form()
    if request.method=='POST':
        form=factorial_form(request.POST)
        if form.is_valid():

         n=form.cleaned_data['n']

         f=factorial_model(n=n)
         f.save()

         result=Factorial.delay(n,f.id)

         f.task_id=result.id
         

         f.save()

         return redirect('factorial')
        else:
            context={
             'form':form
         }

            return render(request,'index.html',context)

    else:
            context={
             'form':form
         }

            return render(request,'index.html',context)

