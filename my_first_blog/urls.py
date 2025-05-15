import os



ADMIN_URL_PATH = os.getenv("ADMIN_URL_PATH")

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path("martha-the-dog-admin/", admin.site.urls),
    path("", include("blog.url"))
]
