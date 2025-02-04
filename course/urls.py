from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path("", views.index, name="course_index"),
    path("<int:course_id>/", views.detail, name="course_detail"),
    path("new/", views.create, name="course_new")
]
