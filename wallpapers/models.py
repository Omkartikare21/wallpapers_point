from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Wallpapers(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="wallpapers", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.CharField(max_length=40)
    tags = models.ManyToManyField(Tag)
    favourites = models.ManyToManyField(
        User, related_name="favourite", default=None, blank=True)
    likes = models.ManyToManyField(User, default=None)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Wallpapers"


class Comments(models.Model):
    user_name = models.CharField(max_length=80)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.user_name} {self.text}"

    class Meta:
        verbose_name_plural = "Comments"
