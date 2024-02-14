from .views import *
from django.urls import path


urlpatterns = [
    path('', TodoApiView.as_view(), name="todos"),
    path('<int:id>', TodoDetailApiView.as_view(), name="todos")
]
