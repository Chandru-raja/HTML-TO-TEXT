from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('html_generator', views.html_generator)
]
