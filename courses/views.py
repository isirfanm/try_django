from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Course
from .forms import CourseModelForm

# Create your views here.


# Based View Class = View
class CourseCreateView(View):
    template_name = "courses/course_create.html"

    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    # get method for GET request
    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)


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
    # def post(self, request, *args, **kwargs):
    #     return render(request, "courses/about.html", {})


# HTTP methods
def my_fbv(request, *args, **kwargs):
    return render("request", "courses/about.html", {})
