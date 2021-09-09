from django.http.response import HttpResponseRedirect
from wallpapers.forms import CommentForm
from django.shortcuts import render
from .models import Wallpapers, Category
from django.urls import reverse


def index(request):
    comment_form = CommentForm(request.POST)
    category = request.GET.get('category')
    if category == None:
        wallpapers = Wallpapers.objects.all()
    else:
        wallpapers = Wallpapers.objects.filter(category__name=category)

    categories = Category.objects.all()

    if comment_form.is_valid():
        comment = comment_form.save()
        return HttpResponseRedirect(reverse("start_page"))

    context = {"categories": categories, "wallpapers": wallpapers,
               "comment_form": CommentForm()}
    return render(request, "wallpapers/index.html", context)


def wallpapers(request, slug):
    wallpapers = Wallpapers.objects.get(slug=slug)
    return render(request, "wallpapers/wallpaper.html", {'wallpaper': wallpapers})
