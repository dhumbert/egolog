from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


def get_datum_types():
    return (
        ('numeric', 'Numeric'),
        ('long_text', 'Long Text'),
        ('short_text', 'Short Text'),
        ('choice', 'Choice'),
        ('multi_choice', 'Multi Choice'),
        ('range', 'Range'),
        ('image', 'Image'),
    )


class Datum(models.Model):
    class Meta:
        verbose_name_plural = "data"

    user = models.ForeignKey(User)
    datum_type = models.CharField(max_length=255, choices=get_datum_types())
    max_value = models.IntegerField(null=True, blank=True)
    min_value = models.IntegerField(null=True, blank=True)
    prompt = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prompt

    def has_choices(self):
        return self.datum_type in ['choice', 'multi_choice']

    def can_have_many_choices(self):
        return self.datum_type in ['multi_choice']

    def has_max_and_min(self):
        return self.datum_type in ['range']

    def has_uploads(self):
        return self.datum_type in ['image']


class Choice(models.Model):
    datum = models.ForeignKey(Datum)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class Response(models.Model):
    class Meta:
        unique_together = ("user", "date", "datum")

    user = models.ForeignKey(User)
    date = models.DateField()
    datum = models.ForeignKey(Datum)
    response = models.TextField()
    choices = models.ManyToManyField(Choice, null=True)
    file = models.FileField(upload_to=settings.UPLOAD_DIR, null=True, blank=True)