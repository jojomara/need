from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('success/', views.success, name='success'), 
    path('', views.kyc_form, name='kyc_form'),
   
]
