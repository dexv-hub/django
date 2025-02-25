from django.urls import path
from . import views
urlpatterns = [
    path('', views.met, name='home'),
    path('about', views.about, name='about'),
    path('events', views.event_details, name='details'),
    path('tickets', views.tickets, name='tickets'),
    path('donate', views.donate, name='donate'),

]