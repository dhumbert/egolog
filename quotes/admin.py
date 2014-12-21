from django.contrib import admin
from quotes.models import Quote, Author


class QuoteAdmin(admin.ModelAdmin):
    list_display = (lambda obj: obj.text[0:50] + '...', 'author', 'source', 'active')


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Author)
