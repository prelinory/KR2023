from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.input_one, name="input_one"),
    path("input_two/<int:n>/", views.input_two, name="input_two"),
]
