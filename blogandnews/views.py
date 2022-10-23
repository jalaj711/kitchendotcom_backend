from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, News, BlogComment
# Create your views here.


def blogandnews(request):
    blogs = Blog.objects.all()
    newss = News.objects.all()
    return render(request, "blogandnews.html", {
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
