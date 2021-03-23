from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",views.index, name="index"),
    path("main/",views.hid,name="main"),
    path("error/",views.error,name="error")
]
