from django.urls import path
from test_map import views


urlpatterns = [
    path("", views.index),
]
