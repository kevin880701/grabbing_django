from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view),
    path('start', views.start_view),
    path('stop', views.stop_view),
    path('status', views.status_view),
]