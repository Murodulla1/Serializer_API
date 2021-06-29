from django.urls import path

from . views import Employes_post, Employes_detail, Ragbat_list, Ragbat_detail


urlpatterns = [
    path('employe/', Employes_post),
    path('employe/<int:pk>/', Employes_detail),
    path('ragbat/', Ragbat_list),
    path('ragbat/<int:pk>/', Ragbat_detail)
]