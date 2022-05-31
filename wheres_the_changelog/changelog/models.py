from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class Changelog(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=1000, unique=True)
    changelog_url = models.URLField(unique=True)

    def __str__(self):
        return self.package_name
