from django.contrib import admin
from django.urls import path
from . import views
from .views import EventList
from .views import EventView
from .views import qr_scanner_view,process_qr
urlpatterns = [
    # path('list/', views.EventList),
    path('list/', EventList.as_view(), name='event-list'),
    path('<int:pk>/', views.EventView),
    # path("scan/",views.scanner, name='scanner'),
    path('scan/', views.qr_scanner_view, name='qr_scanner'),
    path('scan/process/', views.process_qr, name='process_qr'),
    path('book-ticket/<int:user_id>/', views.book_ticket, name='book_ticket'),

    # path('get_qr_data/', views.get_qr_data, name='get_qr_data'),
]
