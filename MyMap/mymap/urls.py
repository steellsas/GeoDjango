from django.urls import path
from .views import map_view


app_name = 'mymap'

urlpatterns = [
    path('map/', map_view),
]