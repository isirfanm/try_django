from django.shortcuts import render
from django.views import View

# Create your views here.


# Based View Class = View
class CourseView(View):
    template_name = "courses/about.html"

    # get method for GET request
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    # post method for POST request
    def post(self, request, *args, **kwargs):
        return render(request, "courses/about.html", {})


# HTTP methods
def my_fbv(request, *args, **kwargs):
    return render("request", "courses/about.html", {})
