from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact_page, name="contact_page"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("sample_service/", views.sample_service, name="sample_service"),
]
