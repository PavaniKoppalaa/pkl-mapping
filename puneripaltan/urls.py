from django.urls import path
from puneripaltan.views import *
app_name='puneripaltan'
urlpatterns=[
    path('pune/',pune,name='pune'),
]