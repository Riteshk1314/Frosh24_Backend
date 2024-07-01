from django.contrib import admin
from django.urls import path
from . import views
from .views import EventList
from .views import EventView
from .views import scanner
urlpatterns = [
    path('list/', views.EventList),
    path('<int:pk>/', views.EventView),
    path("scan/",views.scanner,name="home"),
]
