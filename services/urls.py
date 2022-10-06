from django.urls import path
from services.views import SystemView, EvantView, ServiceView, TableView, RestoranView, MenuView, OrderView, SystemFileView


urlpatterns = [
    path('info/', SystemView.as_view()),
    path('gallery/', SystemFileView.as_view()),
    path('events/', EvantView.as_view()),
    path('restorans/', RestoranView.as_view()),
    path('menus/', MenuView.as_view()),
    path('tables/', TableView.as_view()),
    path('order/', OrderView.as_view()),
    path('services/', ServiceView.as_view()),
]