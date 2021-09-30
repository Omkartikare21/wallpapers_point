from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from wallpapers.forms import CommentForm, RegisterForm
from .models import Comments, Wallpapers, Category
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def Start(request):
    index = Wallpapers.objects.all()[7:8]
    indexloop = Wallpapers.objects.all().order_by("-date")[1:5]
    context = {
        "index": index, "indexloop": indexloop
    }
    return render(request, "wallpapers/index.html", context)


@method_decorator(login_required, name="dispatch")
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


@method_decorator(login_required, name="dispatch")
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


@method_decorator(login_required, name="dispatch")
class WallTags(View):
    def get(self, request):
        wallpapers = Wallpapers.objects.all()
        tag = request.GET.get('tag')
        wallpapers = Wallpapers.objects.filter(
            tags__caption=tag).order_by("-date")
        context = {
            "wallpapers": wallpapers,
            "tag": tag,
        }

        return render(request, "wallpapers/wallTags.html", context)


@method_decorator(login_required, name="dispatch")
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


@login_required
def wallpapers(request, slug):
    fav = bool
    allWallpaper = Wallpapers.objects.all()
    swImg = allWallpaper.order_by("-date")[1:2]
    swImgLoop = Wallpapers.objects.all().order_by("-date")[2:5]
    wallpaper = allWallpaper.get(slug=slug)

    if wallpaper.favourites.filter(id=request.user.id).exists():
        fav = True

    context = {
        'wallpaper': wallpaper,
        "swImg": swImg,
        "tags": wallpaper.tags.all(),
        "swImgLoop": swImgLoop,
        "fav": fav,
    }

    return render(request, "wallpapers/wallpaper.html", context)


@login_required
def search_bar(request):
    search = request.GET.get('search')
    result = Wallpapers.objects.filter(title__icontains=search)
    context = {
        "result": result
    }
    return render(request, "wallpapers/search_bar.html", context)


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()

        context = {
            "form": form,
        }

        return render(request, "wallpapers/Register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            messages.success(
                request, "Congratulations!!! Your Account has been Registered Successfully")
            form.save()

        context = {
            "form": form,
        }
        return render(request, "wallpapers/Register.html", context)


@login_required
def wishlist_list(request):
    lists = Wallpapers.objects.filter(favourites=request.user)

    return render(request, "wallpapers/wishList.html", {"lists": lists})


@login_required
def wishlist_add(request, slug):
    wallpaper = Wallpapers.objects.get(slug=slug)

    if wallpaper.favourites.filter(id=request.user.id).exists():
        wallpaper.favourites.remove(request.user)
    else:
        wallpaper.favourites.add(request.user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
