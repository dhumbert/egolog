from datetime import date, datetime, time, timedelta
import itertools
import random
from django.shortcuts import render, redirect
from data import models as data_models
from quotes import models as quote_models
from data.forms import DataForm


def index(request):
    current_date = date.today()
    prev_day, _ = get_bracketing_dates(current_date)

    quote = random.choice(quote_models.Quote.objects.filter(active=True).all())

    context = {
        'date': current_date,
        'prev_day': prev_day,
        'quote': quote,
    }

    if request.method == 'POST':
        form = DataForm(request.user, data=request.POST, files=request.FILES)

        if form.is_valid():
            for datum in data_models.Datum.objects.filter(user=request.user, active=True):
                response, _ = data_models.Response.objects.get_or_create(date=current_date, user=request.user, datum=datum)
                response.date = current_date
                response.user = request.user
                response.datum = datum

                datum_key = 'datum_{}'.format(datum.id)
                if datum_key in form.cleaned_data:
                    if datum.has_choices():
                        if datum.can_have_many_choices():
                            for choice_response in form.cleaned_data[datum_key]:
                                choice = data_models.Choice.objects.get(pk=choice_response)
                                response.choices.add(choice)
                        else:
                            choice = data_models.Choice.objects.get(pk=form.cleaned_data[datum_key])
                            response.choices.add(choice)
                    elif datum.has_uploads():
                        response.file = request.FILES[datum_key]
                    else:
                        response.response = form.cleaned_data[datum_key]

                    response.save()

            return redirect('index')
        else:
            context['form'] = form
            return render(request, 'frontend/index.html', context)
    else:
        existing_data = {}
        for response in data_models.Response.objects.filter(user=request.user, date=current_date).all():
            if response.datum.has_choices():
                if response.datum.can_have_many_choices():
                    existing_data['datum_{}'.format(response.datum.id)] = []
                    for choice in response.choices.all():
                        existing_data['datum_{}'.format(response.datum.id)].append(choice.id)
                else:
                    existing_data['datum_{}'.format(response.datum.id)] = response.choices.first().id
            elif response.datum.has_uploads():
                existing_data['datum_{}'.format(response.datum.id)] = response.file
            else:
                existing_data['datum_{}'.format(response.datum.id)] = response.response

        fn_field_name = lambda f: f.field.__class__.__name__

        form = DataForm(request.user, data=existing_data)
        fields = sorted(form, key=fn_field_name)  # sort fields for groupby
        field_groups = {x: list(y) for x, y in itertools.groupby(fields, key=fn_field_name)}

        context['field_groups'] = field_groups
        context['existing_data'] = existing_data
        return render(request, 'frontend/index.html', context)


def date_view(request, date_to_view):
    this_date = datetime.strptime(date_to_view, "%Y-%m-%d").date()
    prev_day, next_day = get_bracketing_dates(this_date)

    if this_date == date.today():
        return redirect('index')

    responses = data_models.Response.objects.filter(user=request.user, date=this_date)

    return render(request, 'frontend/date.html', {
        'date': this_date,
        'responses': responses,
        'prev_day': prev_day,
        'next_day': next_day})


def get_bracketing_dates(start_from):
    dt = datetime.combine(start_from, time())
    delta = timedelta(days=1)
    return (dt - delta).strftime('%Y-%m-%d'), (dt + delta).strftime('%Y-%m-%d')