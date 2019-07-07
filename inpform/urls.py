from django.urls import path
from . import views

app_name = 'inpform'

urlpatterns = [

    path('run/', views.run, name='run'),
    path('monitor/', views.monitor, name='monitor'),
]
