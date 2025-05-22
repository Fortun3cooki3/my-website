import os
from decouple import config


from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path(config("ADMIN_URL_PATH"), admin.site.urls),
    path("", include("blog.url"))
]
