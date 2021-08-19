from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sakko/", views.sakko, name="sakko"),
    path("maksu/", views.maksu, name="maksu"),
    path("kulu/", views.kulu, name="kulu"),
]