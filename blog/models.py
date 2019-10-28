from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Article(models.Model):
	name = models.CharField('Author',max_length =200)
	text = models.TextField('Text of the article')
	date = models.DateField('date published')
	def __str__(self):
		return self.name
	def recently(self):
		return self.date > (timezone.now() - datetime.timedelta(days = 7))


class Comment(models.Model):
	article = models.ForeignKey(Article,on_delete =models.CASCADE)
	text = models.TextField('text of the comment')
	date = models.DateField('date of comment')
