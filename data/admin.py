from django.contrib import admin
from data.models import Datum, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class DatumAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'datum_type', 'user', 'active')
    inlines = [ChoiceInline]


admin.site.register(Datum, DatumAdmin)


