from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks',null=True,blank=True)
    title=models.CharField(max_length=200)
    end_date=models.DateField(null=True,blank=True)
    end_time=models.TimeField(null=True,blank=True)
    completed= models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username