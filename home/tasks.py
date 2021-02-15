from celery import shared_task

from .models import factorial_model

from django.core.mail import send_mail






@shared_task
def Factorial(n,id):
    f=factorial_model.objects.get(id=id)
    l=[1,1]
    for i in range(2,n+1):
        l.insert(i,i*l[i-1])
    
    f.result=l[n]
    f.save()
    return f.result









@shared_task
def send_email():
	send_mail('celery beat ', 'This is test for saba company', 'mohammad.moayyeri10@gmail.com', ['mmomiof@yahoo.com'])