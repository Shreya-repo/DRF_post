from django.conf import settings
from django.db import models
from django.utils import timezone
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    readers = models.CharField(max_length = 20, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        
        super(Post, self).save(*args, **kwargs)
    


    class Meta:
        ordering = ['published_date']
