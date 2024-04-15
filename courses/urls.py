from django.urls import path
from .views import CourseCreateView, CourseListView, CourseUpdateView, CourseView

urlpatterns = [
    path(
        "",
        CourseListView.as_view(),
        name="course-list",
    ),
    path(
        "about/",
        CourseView.as_view(template_name="courses/course_about.html"),
        name="course-about",
    ),
    path("<int:id>/", CourseView.as_view(), name="course-detail"),
    path("create/", CourseCreateView.as_view(), name="course-create"),
    path("<int:id>/update/", CourseUpdateView.as_view(), name="course-update"),
]
