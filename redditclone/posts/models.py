from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.TextField(max_length=200)
    url = models.TextField()
    post_date = models.DateField()
    author = models.ForeignKey(User)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def post_date_pretty(self):
        return self.post_date.strftime('%e/%b/%Y')