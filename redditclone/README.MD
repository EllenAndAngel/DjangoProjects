# Create multiply urls.py

- redditclone/urls.py
- add: url(r'^accounts/', include('accounts.urls')),

- create a new urls.py under accounts directory
- accounts/urls.py
- add: app_name = 'accounts', the rest part is same as redditclone/urls.py

- html files
- change url to : {% url 'accounts:login' %}

# next and redirect

- accounts/login.html : 
    {% if request.GET.next %}
        <input type="hidden" name="next" value="{{ request.GET.next }}"/>
    {% endif %}

- accounts/views.py-> user_login

    if 'next' in request.POST:
        return redirect(request.POST['next'])

- posts/views.py

  @login_required
