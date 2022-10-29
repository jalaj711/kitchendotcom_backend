from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, News, BlogComment
from django.http import JsonResponse
# Create your views here.


def serialize(obj):
    dictionary = obj.__dict__
    dictionary.pop('_state', None)
    return dictionary

def blogandnews(request):
    blogs = [serialize(blog) for blog in Blog.objects.all()]
    newss = [serialize(news) for news in News.objects.all()]
    print(blogs, newss)
    return JsonResponse({
        'blogs': blogs,
        'newss': newss,
    })


def blog(request, blogId):
    blog = get_object_or_404(Blog, id=blogId)
    comments = BlogComment.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comments}
    return render(request, 'blog.html', context)


def blog_like(request, blogId):
    blog = get_object_or_404(Blog, id=blogId)
    blog.likes = blog.likes + 1
    blog.save()

    return redirect("blog", blogId=blogId)


def comments(request, blogId):
    if request.method == "POST":
        comment = request.POST.get("comment")
        mail = request.POST.get("mail")
        blog = Blog.objects.get(id=blogId)

        comment = BlogComment(comment=comment, blog=blog, mail=mail)
        comment.save()

    return redirect("blog", blogId=blogId)  # to be changed
