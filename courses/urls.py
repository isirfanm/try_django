from django.urls import path
from .views import CourseView

urlpatterns = [
    path("", CourseView.as_view(template_name="courses/course_about.html"), name="course-list"),
]
