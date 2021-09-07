from django.contrib import admin
from .models import Category, Wallpapers


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )


class WallpapersAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", )
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Wallpapers, WallpapersAdmin)
