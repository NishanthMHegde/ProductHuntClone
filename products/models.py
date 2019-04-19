from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductsModel(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	url = models.TextField()
	image = models.ImageField(upload_to = "images/")
	icon = models.ImageField(upload_to = "images/")
	votes_total = models.IntegerField(default =1)
	publication_date = models.DateTimeField()
	hunter = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def publication_date_pretty(self):
		return self.publication_date.strftime("%b %e %Y")

	def summary(self):
		return self.body[:100]