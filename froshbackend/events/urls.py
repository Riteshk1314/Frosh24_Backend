from django.contrib import admin
from django.urls import path
from . import views
from .views import EventList
from .views import EventView
urlpatterns = [
    path('list/', views.EventList),
    path('<int:id>/', views.EventView),
]
