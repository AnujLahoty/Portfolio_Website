from email.policy import default
from django.db import models

from typing import Iterable

class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

class Project(models.Model):
    serial_no = models.IntegerField(default=99)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    skills = ListField(default=[])
    
    class Meta:
        ordering = ('serial_no',)

    def __str__(self):
        return f"{self.title}"

class Certificate(models.Model):
    title_certificate = models.CharField(max_length=100)
    issuing_org = models.CharField(max_length=250)
    portal = models.CharField(max_length=120)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=1000, default='My description')

    def __str__(self):
        return f"{self.title_certificate}"