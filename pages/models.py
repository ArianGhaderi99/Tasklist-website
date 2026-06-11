from django.db import models

# Create your models here.

class Contactus(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.EmailField()
    message=models.TextField()
    send_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"new message from {self.full_name}"
    
    class Meta:
        verbose_name="Contact message"