from django.contrib import admin
from .models import Blog, News, BlogComment
# Register your models here.

# admin.site.register((Blog, BlogComment))
admin.site.register(News)


class CommentInline(admin.StackedInline):
    model = BlogComment
    extra = 0


@admin.register(Blog)
class Blog_admin(admin.ModelAdmin):
    list_display = ['title', 'likes', 'date']
    inlines = [CommentInline]
