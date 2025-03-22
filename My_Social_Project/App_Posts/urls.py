from django.urls import path
from App_Posts import views
app_name = "App_Posts"

urlpatterns = [
    path("", views.home, name="home"),
    path("liked/<pk>", views.like, name="liked"),
    path("unliked/<pk>", views.unlike, name="unliked"),
    
]