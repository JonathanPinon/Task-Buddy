from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.create_task, name="create_task"),
    path("mine/", views.show_my_tasks, name="show_my_tasks"),
]
