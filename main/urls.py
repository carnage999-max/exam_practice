from . import views
from django.urls import path


urlpatterns = [
    path("cmp/", views.index, name="index"),
    path("cmp/<str:course>/practice", views.course_questions, name="course_questions"),
]
