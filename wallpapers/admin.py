from django.contrib import admin
from .models import Category, Wallpapers, Tag, Comments


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )


class WallpapersAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", )
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date", "category")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "text")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Wallpapers, WallpapersAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentsAdmin)
