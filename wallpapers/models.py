from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class Wallpapers(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to="wallpapers", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Wallpapers"
