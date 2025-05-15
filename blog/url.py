from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("projects", views.projects, name="projects"),
    path("projects/<slug:slug>", views.project, name="project"),
    path("work_experience", views.work_experience, name="work_experience"),
    path("cover_letter", views.refrences, name="cover_letter"),
]