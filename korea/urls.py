from django.urls import path
from . import views

app_name = 'korea'

urlpatterns = [
    path('', views.index, name='index'),
]