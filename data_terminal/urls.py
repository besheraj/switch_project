from django.urls import path
from . import views

urlpatterns = [
    path('showdata/', views.showdata, name='showdata'),
    path('csv_upload/', views.csv_upload, name="csv_upload"),


]
