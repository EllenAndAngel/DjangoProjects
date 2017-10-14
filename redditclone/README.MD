# Create multiply urls.py

- redditclone/urls.py
- add: url(r'^accounts/', include('accounts.urls')),

- create a new urls.py under accounts directory
- accounts/urls.py
- add: app_name = 'accounts', the rest part is same as urls.py under redditclone

- html files
- change url to : {% url 'accounts:login' %}


