from django.db import models

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	def __init__(self, arg):
		super(Post, self).__init__()
		self.arg = arg
	
	title = models.CharField(max_length = 250)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'media/')
	body = models.TextField()