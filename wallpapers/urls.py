from django.urls import path
from . import views

urlpatterns = [

    path('', views.Start, name="index"),
    path("home/", views.HomePage.as_view(), name="home"),

    path("home", views.WallCategory.as_view(), name="wallCategories"),
    path('all-categories/', views.AllCategories.as_view(), name="start_page"),

    path('wallpapers/<slug:slug>', views.wallpapers, name="detail"),
    path('search', views.search_bar, name="searchbar"),


]
