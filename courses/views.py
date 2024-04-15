from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from .models import Course
from .forms import CourseModelForm


# Create your views here.
# Based View Class = View
class CourseObjectMixin:
    model = Course
    lookup = "id"

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        object = None
        if id:
            object = get_object_or_404(self.model, id=id)
        return object


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
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        object = self.get_object()
        if object:
            form = CourseModelForm(instance=object)
            context["form"] = form
            context["object"] = object
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        object = self.get_object()
        if object:
            form = CourseModelForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
            context["form"] = form
            context["object"] = object
        return render(request, self.template_name, context)


class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        object = self.get_object()
        if object:
            context["object"] = object
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        object = self.get_object()
        if object:
            object.delete()
            return redirect(reverse("course-list"))
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/course_list.html"
    # queryset = Course.objects.all()

    def get_queryset(self):
        return Course.objects.all()

    # get method for GET request
    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)


class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"

    # get method for GET request
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id:
            object = self.get_object()
            context["object"] = object
        return render(request, self.template_name, context)

    # post method for POST request
    # def post(self, request, *args, **kwargs):
    #     return render(request, "courses/about.html", {})


# HTTP methods
def my_fbv(request, *args, **kwargs):
    return render("request", "courses/about.html", {})
