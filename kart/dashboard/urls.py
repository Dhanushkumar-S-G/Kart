from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/', views.log_out, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('explore/',views.explore, name="explore"),
    path('lend/', views.lend, name="lend"),
    path('view-profile/<str:roll>', views.view_profile, name="view_profile")
]
