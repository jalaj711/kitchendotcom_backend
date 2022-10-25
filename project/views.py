from django.http import JsonResponse
from project.models import Project, Video, Design, Feedback

# Create your views here.

def serialize(obj):
    dictionary = obj.__dict__
    dictionary.pop('_state', None)
    return dictionary


def projectList(request):
    videos = Video.objects.all()
    designs = Design.objects.all()
    feedbacks = Feedback.objects.all()
    ongoing_projects = Project.objects.filter(full_complete=False)
    complete_projects = Project.objects.filter(full_complete=True)
    return JsonResponse({
        'ongoing_projects': [serialize(proj) for proj in ongoing_projects],
        'complete_projects': [serialize(proj) for proj in complete_projects],
        'videos': [serialize(video) for video in videos],
        'designs': [serialize(design) for design in designs],
        'feedbacks': [serialize(feedback) for feedback in feedbacks]
    })


# def projectDetails(request, id):
#     project = get_object_or_404(Project, id=id)
#     print(project.name)
#     photos = PostImage.objects.filter(project=project)
#     return render(request, 'project_details.html', {
#         'project': project,
#         'photos': photos
#     })


# def projectDetails(request, projectId):
#     try:
#         context = {}
#         __project = Project.objects.get(id=projectId)
#         # __project = Project.objects.filter(Project=__project)
#         context = {'project': __project}
#     # __project =
#         print(__project)
#         return render( request, "project_details.html", context)
#     except:
#         print("not found")
#         return render( request, "project_details.html")
# def projectList(request):
#     posts = Project.objects.all()
#     return render(request, 'project_gallery.html', {'posts':posts})
