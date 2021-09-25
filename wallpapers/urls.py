from django.urls import path
from . import views

urlpatterns = [
    # index
    path('', views.start.as_view(), name="start_page"),
    path('wallpapers/<slug:slug>', views.wallpapers, name="detail"),
    path('search', views.search_bar, name="searchbar")
]
