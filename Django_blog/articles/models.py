from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    date = models.DateTimeField()
    likes = models.TextField()

    def __str__(self):
        return self.title
