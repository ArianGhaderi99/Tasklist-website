from django.shortcuts import render,redirect
from django.contrib import messages
from pages.models import Contactus
# Create your views here.
def home_view(request):
    return render(request,template_name="pages/home.html")


def about_view(request):
    return render(request,template_name="pages/about.html")


def contact_view(request):
    if request.method == "POST":
        full_name= request.POST.get("full_name")
        email= request.POST.get("email")
        message= request.POST.get("message")
        Contactus.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )

        messages.success(request, "your message has been sent successfully")
        return redirect("pages:contact")
    return render(request,template_name="pages/contact.html")

