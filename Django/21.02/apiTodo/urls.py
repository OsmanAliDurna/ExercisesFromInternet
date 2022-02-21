from django.urls import path
from .views import home, todolist, todocreate


urlpatterns = [
    path('', home),
    path('todolist/', todolist),
    path('todocreate/', todocreate),
]
