from django.shortcuts import render, redirect
from django.core import serializers
from . import models
from django.http import Http404, JsonResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def gallery(request):
    data = serializers.serialize('json', models.Event.objects.all())
    return JsonResponse(data, safe=False)


def post_create(request):
    data = serializers.serialize('json')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        event_location = request.POST.get('event_location')
        event_date = request.POST.get('event_date')
        publication_date = request.POST.get('publication_date')
        if not title or not description or not event_location or not event_date:
            data['errors'] = {
                'Missed field': 'Is required'
            }
        else:
            event = models.Event.objects.create(
                title=title,
                description=description,
                image=image,
                event_location=event_location,
                event_date=event_date,
                publication_date=publication_date
            )
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
        post = models.Event.objects.get(pk=pk)
    except models.Event.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    data = dict()
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if not title:
            data['errors'] = {
                'title': 'Is required'
            }
        else:
            post.title = title
            post.body = body
            post.save()
            return redirect('post_show', pk=post.pk)
    return render(request, 'semond/post_update.html', data)


def post_delete(request, pk):
    try:
        post = models.Event.objects.get(pk=pk)
    except models.Event.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'semond/post_delete.html')
