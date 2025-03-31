import django.db.models


class Task(django.db.models.Model):
    name = django.db.models.CharField('name')
