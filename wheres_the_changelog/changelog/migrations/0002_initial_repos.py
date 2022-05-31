from django.db import migrations


def load_initial_repos(apps, schema_editor):
    Repository = apps.get_model("changelog", "Repository")
    Repository.objects.create(name="PyPI", url="https://pypi.org/")
    Repository.objects.create(name="npm", url="https://www.npmjs.com/")


class Migration(migrations.Migration):

    dependencies = [
        ("changelog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_initial_repos, migrations.RunPython.noop),
    ]
