from django.contrib import admin
from django.urls import path
from .views import PhoneView, verify_view, verify_code_view, profile_view, add_invitation_view

urlpatterns = [
    path('auth/', verify_view),
    path('verify_code/', verify_code_view),   
    path('profile/', profile_view),
    path('add_invitation/', add_invitation_view),
    

]
