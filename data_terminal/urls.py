from django.urls import path
from . import views

urlpatterns = [
    path('showdata/', views.showdata, name='showdata'),

]