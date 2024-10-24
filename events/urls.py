from django.urls import path

# importing the views file
from . import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
]
