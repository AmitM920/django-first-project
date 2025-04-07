
from django.contrib import admin
from django.urls import path
from myfirstdjango import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("about-us/",views.aboutUs,name="about"),
    path("course/",views.course ),
    path("course/<int:courseid>",views.CourseById), 
    # slug data is amit-mehta , we can use str also instead of int--above url is a dynamic one
    path("",views.homePage, name="home"), # home is the name of the url, we can use it in templates to refer this url
    path("contact/",views.contact, name="contact"),
    path("userform/",views.userForm, name="userform")
]
