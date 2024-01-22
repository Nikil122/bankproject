from django.urls import path
from . import views
app_name='bank_app'

urlpatterns = [
    path('', views.index,name='index'),
    path('index', views.index,name='index'),
]
