from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),]
    # Add more patterns as needed