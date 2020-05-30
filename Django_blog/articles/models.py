from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    createdBy = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title
