from django.urls import path
from pages import views

app_name="pages"


urlpatterns = [
    path('about/',views.about_view,name="about"),
    path('contact',views.contact_view,name="contact"),
    path('',views.home_view,name="home"),
]