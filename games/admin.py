from django.contrib import admin
from .models import Category, Game, GameScreenshots


class GameScreenshotsInline(admin.TabularInline):
    model = GameScreenshots
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GameScreenshotsInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameScreenshots)