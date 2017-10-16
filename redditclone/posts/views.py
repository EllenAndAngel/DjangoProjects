from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Posts
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    posts = Posts.objects.order_by('-votes')
    return render(request, 'posts/home.html', {'posts': posts})


@login_required
def add(request):
    if request.method == 'POST':

        if request.POST['title'] and request.POST['url']:
            post = Posts()
            post.title = request.POST['title']
            url = request.POST['url']
            if url.startswith('http://') or url.startswith('https://'):
                post.url = url
            else:
                post.url = 'http://' + url

            post.post_date = timezone.datetime.now()
            post.author = request.user
            post.save()

            return redirect('home')

        else:
            return render(request, 'posts/addpost.html',
                          {'error': 'ERROR: You must include a title and a URL to create a post!'})

    else:

        return render(request, 'posts/addpost.html')


def upvote(request, pk):
    post = Posts.objects.get(pk=pk)
    post.votes += 1
    post.save()

    return redirect('home')


def downvote(request, pk):
    post = Posts.objects.get(pk=pk)
    if post.votes == 0:
        post.votes = 0
    else:
        post.votes -= 1
    post.save()

    return redirect('home')
