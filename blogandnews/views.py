from django.shortcuts import get_object_or_404
from .models import Blog, News, BlogComment
from django.http import JsonResponse
import json
# Create your views here.


def serialize(obj):
    dictionary = obj.__dict__
    dictionary.pop('_state', None)
    return dictionary


def blogandnews(request):
    blogs = [serialize(blog) for blog in Blog.objects.all()]
    newss = [serialize(news) for news in News.objects.all()]
    return JsonResponse({
        'blogs': blogs,
        'newss': newss,
    })


def blog(request, blogId):
    blog = get_object_or_404(Blog, id=blogId)
    comments = BlogComment.objects.filter(blog=blogId)
    return JsonResponse({
        'blog': serialize(blog),
        'comments': [serialize(comment) for comment in comments]
    })


def blog_like(request, blogId):
    blog = get_object_or_404(Blog, id=blogId)
    blog.likes = blog.likes + 1
    blog.save()

    return JsonResponse({
        'success': True,
        'n_likes': blog.likes,
    })


def comments(request, blogId):
    if request.method == "POST":
        data = json.loads(request.body)
        comment = data.get("comment")
        mail = data.get("mail")
        blog = Blog.objects.get(id=blogId)

        comment = BlogComment(comment=comment, blog=blog, mail=mail)
        comment.save()

    return JsonResponse({
        'success': True
    })
