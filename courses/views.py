from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Course
# Create your views here.

# define a view
def index(request):
    courses = Course.objects    # pull objects from DB
    return render(request, 'courses/index.html', {'courses':courses})


def detail(request, course_id):
    course_detail = get_object_or_404(Course, pk=course_id) # name of model, primary key: if not found, return 404
    return render(request, 'courses/detail.html', {'course': course_detail})

