from django.urls import path
from specific.views import *

app_name='specific'

urlpatterns=[
    path('pavan/',pavan,name='pavan'),
    path('bhuvi/',bhuvi,name='bhuvi'),
]