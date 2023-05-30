from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.settings, name="settings"),
    path('accounts/', views.all_users, name='personal'),
    path('<str:username>/', views.profile, name="profile"),
]
