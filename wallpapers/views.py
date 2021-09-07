from django.shortcuts import render
from .models import Wallpapers, Category
# Add Comment later


def index(request):
    category = request.GET.get('category')
    if category == None:
        wallpapers = Wallpapers.objects.all()
    else:
        wallpapers = Wallpapers.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {"categories": categories, "wallpapers": wallpapers}
    return render(request, "wallpapers/index.html", context)


def wallpapers(request, slug):
    wallpapers = Wallpapers.objects.get(slug=slug)
    return render(request, "wallpapers/wallpaper.html", {'wallpaper': wallpapers})
