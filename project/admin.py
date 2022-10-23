from django.contrib import admin

# Register your models here.
from project.models import Project, Video, Feedback, Design, PostImage

admin.site.register(Video)
admin.site.register(Design)
admin.site.register(Feedback)
# admin.site.register(Project)
# admin.site.register(PostImage)

#  For adding multipleimages in Project Model
class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Project
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass