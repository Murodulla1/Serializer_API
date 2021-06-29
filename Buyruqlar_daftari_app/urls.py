from django.urls import path

from .views import Comands, Putcomand

urlpatterns = [
    path('Com/', Comands),
    path('Put/', Putcomand),

]