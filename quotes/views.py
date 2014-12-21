import random
import json
from django.http import HttpResponse
from quotes.models import Quote


def random_quote(request):
    quotes = Quote.objects.filter(user=request.user, active=True).all()
    quote = random.choice(quotes)

    return HttpResponse(json.dumps(quote.as_dict()))

