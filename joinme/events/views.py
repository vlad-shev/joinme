from django.shortcuts import render, redirect
from django.core import serializers
from . import models
from django.http import Http404, HttpResponse, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    return render(request, 'home.html')


def gallery(request):
    data = serializers.serialize('json', models.Event.objects.all())
    return JsonResponse(data, safe=False)

@csrf_exempt
def post_create(request):
    data = dict()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_location = request.POST.get('event_location')
        event_date = request.POST.get('event_date')
        if not (title or description or event_location or event_date):
            data['errors'] = {
                'something': 'Is required'
            }
        else:
            event = models.Event.objects.create(
                title=title,
                description=description,
                event_date=event_date,
                event_location=event_location)
            return redirect('post_show', pk=event.pk)
    return render(request, 'post_create.html', data)


def post_show(request, pk):
    try:
        event = models.Event.objects.get(pk=pk)
    except models.Event.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    data = serializers.serialize('json',
        [event]
    )
    return JsonResponse(data, safe=False)


def post_update(request, pk):
    try:
        event = models.Event.objects.get(pk=pk)
    except models.Event.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    data = dict()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('body')
        if not title:
            data['errors'] = {
                'title': 'Is required'
            }
        else:
            event.title = title
            event.description = body
            event.save()
            return redirect('post_show', pk=event.pk)
    return render(request, 'semond/post_update.html', data)


def post_delete(request, pk):
    try:
        event = models.Event.objects.get(pk=pk)
    except models.Event.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    if request.method == 'POST':
        event.delete()
        return redirect('blog')
    return render(request, 'semond/post_delete.html')
