from django.db import models

# Create your models here.

class Employee(models.Model):
    person = models.CharField(max_length=40)
    date = models.DateField()
    temp = models.IntegerField(null=True)
    dev = models.CharField(max_length=40, null=True)

    def __str__(self):
        return str(self.person)

class Temp(models.Model):
    tempt = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    emp = models.CharField(max_length=50, null=True)
    emp_tempt = models.IntegerField(null=True)


    def __str__(self):
        return str(self.emp_tempt)

class Dev(models.Model):
    devi = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    devi_name = models.CharField(max_length=50, null=True)


    def __str__(self):
        return str(self.devi_name)





