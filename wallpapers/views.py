from django.http.response import HttpResponseRedirect
from wallpapers.forms import CommentForm
from django.shortcuts import render
from .models import Comments, Wallpapers, Category
from django.urls import reverse
from django.views import View


class start(View):
    def get(self, request):
        categories = Category.objects.all()
        wallpapers = Wallpapers.objects.all()
        category = request.GET.get('category')
        if category == None:
            wallpapers = Wallpapers.objects.all()
        else:
            wallpapers = Wallpapers.objects.filter(category__name=category)

        categories = Category.objects.all()
        context = {"categories": categories, "wallpapers": wallpapers,
                   "comment_form": CommentForm(), "comments": Comments.objects.all().order_by("-id")}
        return render(request, "wallpapers/index.html", context)

    def post(self, request):
        comment_form = CommentForm(request.POST)
        categories = Category.objects.all()
        wallpapers = Wallpapers.objects.all()

        if comment_form.is_valid():
            comment = comment_form.save()
            return HttpResponseRedirect(reverse("start_page"))
        else:
            context = {"categories": categories, "wallpapers": wallpapers,
                       "comment_form": CommentForm(), "comments": Comments.objects.all().order_by("-id")}
            return render(request, 'start_page', context)


# def index(request):
#     comment_form = CommentForm(request.POST)
#     category = request.GET.get('category')
#     if category == None:
#         wallpapers = Wallpapers.objects.all()
#     else:
#         wallpapers = Wallpapers.objects.filter(category__name=category)

#     categories = Category.objects.all()

#     if comment_form.is_valid():
#         return HttpResponseRedirect(reverse("start_page"))

#     context = {"categories": categories, "wallpapers": wallpapers,
#                "comment_form": CommentForm()}
#     return render(request, "wallpapers/index.html", context)

#         comment = comment_form.save()

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


class HomePage(View):

    def get(self, request):
        new = Wallpapers.objects.filter(
            category__name__icontains="3D")[:1]
        return render(request, "wallpapers/homepage.html", {"new": new})
