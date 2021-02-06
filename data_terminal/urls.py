from django.urls import path
from . import views

urlpatterns = [
    path('charts/', views.charts, name='charts'),
    path('csv_upload/', views.csv_upload, name="csv_upload"),


]
