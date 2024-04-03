from django.urls import path
from patnapirates.views import *
app_name='hi'
urlpatterns=[
    path('patna/',patna,name='patna'),
]