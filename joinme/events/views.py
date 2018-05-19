from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.


def home(request):
    return render(request, 'home.html')


def gallery(request):
    posts = models.Post.objects.all().order_by('-updated_at')
    data = dict(
        posts=posts
    )
    return render(request, 'gallery.html', data)


def post_create(request):
    data = dict()
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if not title:
            data['errors'] = {
                'title': 'Is required'
            }
        else:
            post = models.Post.objects.create(title=title, body=body)
            return redirect('post_show', pk=post.pk)

    return render(request, 'post_create.html', data)


def post_show(request):
    try:
        post = models.Post.objects.get(pk=pk)
    except models.Post.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    data = dict(
        post=post
    )
    return render(request, 'post_show.html', data)


def post_update(request):
    try:
        post = models.Post.objects.get(pk=pk)
    except models.Post.DoesNotExist:
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
        post = models.Post.objects.get(pk=pk)
    except models.Post.DoesNotExist:
        raise Http404('Post with id <{}> does not exist.'.format(pk))
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'semond/post_delete.html')
