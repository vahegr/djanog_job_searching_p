from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(models.Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    display = ('category_to_str', 'title', 'slug', 'publish', 'status', 'thumbnail')
    list_filter = ('status',)
    search_fields = ('title', 'description')

    # ordering=['-status','-publish']

    def category_to_str(self, obj):
        return ", ".join(category.title for category in obj.category.all())

