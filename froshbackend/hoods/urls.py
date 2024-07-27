from django.urls import path
from hoods import views

urlpatterns = [
    path('dashboard/', views.hood_leaderboard)
    # path('')
]

