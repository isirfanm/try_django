from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Course

# Create your views here.


# Based View Class = View
class CourseView(View):
    template_name = "courses/course_detail.html"

    # get method for GET request
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id:
            object = get_object_or_404(Course, id=id)
            context["object"] = object
        return render(request, self.template_name, context)

    # post method for POST request
    def post(self, request, *args, **kwargs):
        return render(request, "courses/about.html", {})


# HTTP methods
def my_fbv(request, *args, **kwargs):
    return render("request", "courses/about.html", {})
