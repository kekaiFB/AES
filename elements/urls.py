from django.urls import path
 
from .views import *
 
app_name = 'elements'

urlpatterns = [
    path('', ElementsView.as_view(), name='elements_list'),
]