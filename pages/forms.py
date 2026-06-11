from django import forms
from pages.models import Contactus

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=['full_name',"email","message"]
        widgets={
            "full_name": forms.TextInput(attrs={'class': 'form-control','placeholder': 'your full name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control','placeholder': 'your@email.com'}),
            "message": forms.Textarea(attrs={'class': 'form-control','rows': 4})
        }