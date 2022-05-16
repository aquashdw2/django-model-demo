from django.urls import path

from delivery import views


urlpatterns =[
    path("diner/", views.diner_query)
]
