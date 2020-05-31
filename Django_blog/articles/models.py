from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


@property
def num_likes(self):
    return self.liked.all().count()

