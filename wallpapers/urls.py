from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="start_page"),
    path('wallpapers/<slug:slug>', views.wallpapers, name="detail")
]
