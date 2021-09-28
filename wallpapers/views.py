from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from wallpapers.forms import CommentForm, CustomerRegisterForm  # ,WallRegisterForm
from .models import Comments, Wallpapers, Category
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required


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


class AllCategories(View):
    def get(self, request):
        categories = Category.objects.all()
        count = 0
        wallpapers = Wallpapers.objects.all()
        category = request.GET.get('category')

        if category == None:
            wallpapers = Wallpapers.objects.all().order_by("-date")[1:]

            # count = Wallpapers.objects.filter(
            #     category__name__icontains=category).count()

        else:
            wallpapers = Wallpapers.objects.filter(
                category__name=category).order_by("-date")

        print(count)

        context = {"categories": categories, "wallpapers": wallpapers,
                   "comment_form": CommentForm(), "comments": Comments.objects.all().order_by("-id"), "count": count}
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
    # wallpaper = Wallpapers.objects.get(slug=slug)
    allWallpaper = Wallpapers.objects.all()
    swImg = allWallpaper.order_by("-date")[1:2]
    swImgLoop = Wallpapers.objects.all().order_by("-date")[2:5]
    wallpaper = allWallpaper.get(slug=slug)

    context = {
        'wallpaper': wallpaper,
        "swImg": swImg,
        "tags": wallpaper.tags.all(),
        "swImgLoop": swImgLoop,
    }

    return render(request, "wallpapers/wallpaper.html", context)


def search_bar(request):
    search = request.GET.get('search')
    result = Wallpapers.objects.filter(title__icontains=search)
    context = {
        "result": result
    }
    return render(request, "wallpapers/search_bar.html", context)


# class Register(View):
#     def get(self, request):
#         form = WallRegisterForm()
#         context = {
#             "form": form
#         }
#         return render(request, "wallpapers/register.html", context)

#     def post(self, request):
#         form = WallRegisterForm(request.POST)

#         if form.is_valid():
#             messages.success(request, "You have sucessfully created account")
#             form.save()

#         context = {
#             "form": form,
#         }
#         return render(request, "wallpapers/register.html", context)


class CustomRegisterView(View):

    def get(self, request):
        form = CustomerRegisterForm()

        context = {
            "form": form,
        }

        return render(request, "wallpapers/customerRegistration.html", context)

    def post(self, request):
        form = CustomerRegisterForm(request.POST)

        if form.is_valid():
            messages.success(
                request, "Congratulations You are Account Registered Successfully")
            form.save()

        context = {
            "form": form,
        }

        return render(request, "wallpapers/customerRegistration.html", context)


@login_required
def wishlist_list(request):
    lists = Wallpapers.objects.filter(favourites=request.user)

    return render(request, "wallpapers/wishList.html", {"lists": lists})


@login_required
def wishlist_add(request, slug):
    movie = Wallpapers.objects.get(slug=slug)

    if movie.favourites.filter(id=request.user.id).exists():
        movie.favourites.remove(request.user)
    else:
        movie.favourites.add(request.user)

    # return HttpResponseRedirect(reverse("wishlist"))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
