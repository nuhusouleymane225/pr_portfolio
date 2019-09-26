from django.shortcuts import render
from . models import Project
from . models import Detail

# Create your views here.
def project_index(request):
    context = {
        'project': Project.objects.all()
        }
    return render(request, 'project_index.html', context)


def project_detail(request,pk):
    variable = {
        'detail': Detail.objects.get(pk=pk)
        }
    return render(request,'project_detail.html', variable)