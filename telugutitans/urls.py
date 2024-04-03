from django.urls import path
from telugutitans.views import *
app_name='telugutitans'
urlpatterns=[
    path('telugu/',telugu,name='telugu'),
]