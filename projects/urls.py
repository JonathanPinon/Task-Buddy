from django.urls import path
from . import views


urlpatterns = [
    path("", views.list_projects, name="list_projects"),
    path("<int:id>/", views.show_project, name="show_project"),
]
