from django.http.response import HttpResponseRedirect
from wallpapers.forms import CommentForm
from django.shortcuts import render
from .models import Comments, Wallpapers, Category
from django.urls import reverse
from django.views import View


def Start(request):
    index = Wallpapers.objects.all()[:1]
    indexloop = Wallpapers.objects.all().order_by("-date")[1:5]
    context = {
        "index": index, "indexloop": indexloop
    }
    return render(request, "wallpapers/index.html", context)


class HomePage(View):
    def get(self, request):
        filteredanimal = Wallpapers.objects.filter(
            category__name__icontains="Animal").order_by("-date")[:1]

        filtered3D = Wallpapers.objects.filter(
            category__name__icontains="3D").order_by("-date")[:1]

        filteredanime = Wallpapers.objects.filter(
            category__name__icontains="Anime").order_by("-date")[:1]

        filteredcity = Wallpapers.objects.filter(
            category__name__icontains="City").order_by("-date")[:1]

        filteredfantasy = Wallpapers.objects.filter(
            category__name__icontains="Fantasy").order_by("-date")[:1]

        filteredholidays = Wallpapers.objects.filter(
            category__name__icontains="Holidays").order_by("-date")[:1]

        filteredcars = Wallpapers.objects.filter(
            category__name__icontains="Cars").order_by("-date")[:1]

        filterednature = Wallpapers.objects.filter(
            category__name__icontains="Nature").order_by("-date")[:1]

        filteredart = Wallpapers.objects.filter(
            category__name__icontains="Art").order_by("-date")[:1]

        filteredspace = Wallpapers.objects.filter(
            category__name__icontains="Space").order_by("-date")[:1]

        context = {
            "filteredanimal": filteredanimal,
            "filtered3D": filtered3D,
            "filteredanime": filteredanime,
            "filteredcity": filteredcity,
            "filteredcars": filteredcars,
            "filteredfantasy": filteredfantasy,
            "filteredholidays": filteredholidays,
            "filterednature": filterednature,
            "filteredcars": filteredcars,
            "filteredspace": filteredspace,
            "filteredart": filteredart

        }

        return render(request, "wallpapers/homepage.html", context)


class WallCategory(View):
    def get(self, request):
        wallpapers = Wallpapers.objects.all()
        category = request.GET.get('category')
        wallpapers = Wallpapers.objects.filter(
            category__name=category).order_by("-date")
        context = {
            "wallpapers": wallpapers,
            "category": category,
        }

        return render(request, "wallpapers/wallCategories.html", context)


class AllCategories(View):
    def get(self, request):
        categories = Category.objects.all()
        wallpapers = Wallpapers.objects.all()
        category = request.GET.get('category')
        if category == None:
            wallpapers = Wallpapers.objects.all().order_by("-date")[1:]
        else:
            wallpapers = Wallpapers.objects.filter(
                category__name=category).order_by("-date")

        context = {"categories": categories, "wallpapers": wallpapers,
                   "comment_form": CommentForm(), "comments": Comments.objects.all().order_by("-id")}
        return render(request, "wallpapers/all_categories.html", context)

    def post(self, request):
        comment_form = CommentForm(request.POST)
        categories = Category.objects.all()
        wallpapers = Wallpapers.objects.all()

        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse("start_page"))
        else:
            context = {"categories": categories, "wallpapers": wallpapers,
                       "comment_form": CommentForm(), "comments": Comments.objects.all().order_by("-id")}
            return render(request, 'start_page', context)


def wallpapers(request, slug):
    wallpapers = Wallpapers.objects.get(slug=slug)
    context = {
        'wallpaper': wallpapers,
        'tags': wallpapers.tags.all()
    }
    return render(request, "wallpapers/wallpaper.html", context)


def search_bar(request):
    search = request.GET.get('search')
    result = Wallpapers.objects.filter(title__icontains=search)
    context = {
        "result": result
    }
    return render(request, "wallpapers/search_bar.html", context)
