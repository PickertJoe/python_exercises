"""Defining URL patterns for mountain_log"""

from django.urls import path
from . import views

app_name = "mountain_log"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Topics page
    path('mountains/', views.mountains, name='mountains'),

    # Detail page for a single topic
    path('mountains/<int:mountain_id>', views.mountain, name='mountain'),
]
