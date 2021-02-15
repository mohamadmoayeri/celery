from django.db import models

# Create your models here.



class factorial_model(models.Model):
    task_id=models.CharField(max_length=50)

    n=models.IntegerField()

    result=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return f' factorial({self.n})={self.result}'
    