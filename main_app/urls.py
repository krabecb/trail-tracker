from django.urls import path
from . import views

#Similar to app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]