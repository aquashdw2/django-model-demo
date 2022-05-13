from django.urls import path
from test_map import views


urlpatterns = [
    path("", views.index),
    path("save-points/", views.save_points),
    path("get-points/", views.get_points),
]
