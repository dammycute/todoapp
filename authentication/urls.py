from authentication import views
from django.urls import path


urlpatterns = [
    path('register', views.RegisterApiView.as_view(), name= "register"),
    # path('login', views.LoginApiView.as_view(), name= "login"),
    # path('user', views.AuthUserApiView.as_view(), name= "user"),
]
