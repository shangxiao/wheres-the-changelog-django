from django.contrib import admin

from .models import Changelog, Repository


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Changelog)
class ChangelogAdmin(admin.ModelAdmin):
    ...
