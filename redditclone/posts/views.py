from django.shortcuts import render
from django.utils import timezone
from .models import Posts
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'posts/home.html')


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

            return render(request,'posts/home.html')



    else:

        return render(request, 'posts/addpost.html')
