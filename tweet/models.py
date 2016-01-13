from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Tweet_post(models.Model):

    class Meta:
        verbose_name_plural = 'Tweet'
        ordering = ['publish_timestamp']

    STATUS = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )
    tweet = models.CharField(max_length=255, 
        choices=STATUS, default=STATUS[0][0])
    publish_timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User)
    message = models.TextField(max_length=255)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.message


class tweet_text(models.Model):
    text=models.CharField(max_length=120,blank=True,null=True)
    def __unicode__(self):
        return self.text


