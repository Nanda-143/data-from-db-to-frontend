from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return self.dname
    
class emp(models.Model):
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    job=models.CharField(max_length=100)
    comm=models.IntegerField()
    def __str__(self):
        return self.ename
    
