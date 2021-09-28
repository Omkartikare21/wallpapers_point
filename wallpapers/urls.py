from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from wallpapers.forms import LoginForm
urlpatterns = [

    path('', views.Start, name="index"),
    path("home/", views.HomePage.as_view(), name="home"),

    path("home", views.WallCategory.as_view(), name="wallCategories"),
    path("tags/", views.WallTags.as_view(), name="tags"),
    path('all-categories/', views.AllCategories.as_view(), name="start_page"),

    path('wallpapers/<slug:slug>', views.wallpapers, name="detail"),
    path('search', views.search_bar, name="searchbar"),

    # path('register/', views.Register.as_view(), name="register"),
    path("register/", views.CustomRegisterView.as_view(), name="register"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="wallpapers/login.html",
         authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),

    path("/wishlist/", views.wishlist_list, name="wishlist"),
    path("wishlist/<slug:slug>", views.wishlist_add, name="wishlist_add"),
]
