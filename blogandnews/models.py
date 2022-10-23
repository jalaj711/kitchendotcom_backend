from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now


class Blog(models.Model):
    title = models.CharField(max_length=100, default="Title")
    author = models.CharField(max_length=100, default="admin")
    date = models.DateField(auto_created=True)
    image = models.FileField(upload_to="blogs/", max_length=100)
    content = RichTextField()
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class News(models.Model):
    heading = models.CharField(max_length=100, default="Title")
    author = models.CharField(max_length=100, default="admin")
    date = models.DateField(auto_now=True)
    image = models.FileField(upload_to="blogs/", max_length=100)
    content = RichTextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.heading


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = RichTextField()
    mail = models.EmailField(max_length=254)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return self.blog.title
