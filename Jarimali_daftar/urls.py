from django.urls import path

from . views import fines_list, fines_detail

urlpatterns = [
    path('fin_list/', fines_list),
    path('fin_det/', fines_detail)
]